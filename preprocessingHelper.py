import numpy as np
from PIL import Image
from logHelper import ExecuteWithLogs
import os

TARGET_SIZE = (512, 512)

def PerformPreprocessing(files, log_file_path): 
    for i, file in enumerate(files):
        print("{0}/{1} {2}".format(i, len(files), file))
        PerformPreprocessingForSingleFile(file, log_file_path)

def PerformPreprocessingForSingleFile(file, log_file_path):
    f = open(file, 'rb')
    img_str = f.read()

    isMask = "MM" in file

    # converting to a int8/int16 numpy array
    ct_image_as_vector = np.fromstring(img_str, dtype=np.dtype(bool)) if isMask else np.fromstring(img_str, dtype=np.int16)

    #layering
    layer_dimensions = (512, 512)
    layer_size = layer_dimensions[0]*layer_dimensions[1]
    layers_count = int(len(ct_image_as_vector) / layer_size)
    ct_image_layered = np.reshape(ct_image_as_vector, (layers_count, layer_size))

    # get the image and plot it
    for i, layer in enumerate(ct_image_layered):            
        print("{0}/{1}".format(i, len(ct_image_layered)))
        ExecuteWithLogs("Preprocessing for layer #{0}".format(i), log_file_path, lambda _ = None: PerformPreprocessingForSingleLayer(file, i, layer, isMask))   


def PerformPreprocessingForSingleLayer(file, i, layer, isMask):
    #layer.byteswap(inplace=True)        
    #Normalize function
    if (isMask):  
        layer = layer * 255 #https://stackoverflow.com/questions/47290668/image-fromarray-just-produces-black-image
    else:  
        #uint8
        newMin = 0
        newMax = 255 
        newRange = (newMax - newMin)  

        #range extracted from layer itself
        oldMin = layer.min()
        oldMax = layer.max()
        oldRange = (oldMax - oldMin) 

        normalize = lambda x: int((((x - oldMin) * newRange) / oldRange) + newMin)
        npNormalize = np.vectorize(normalize)
        layer = npNormalize(layer)
    layer = np.reshape(layer, (512, 512))
    image = Image.fromarray(layer.astype(np.uint8), "L") 
    image.save("{0}_{1}.png".format(file, i), "PNG")

def SliceListEvenly(source_list, slice_length):
    for i in range(0, len(source_list), slice_length):
        yield source_list[i:i + slice_length]

def CalculateMaskSizeLevels(level_count):    
    png_files = list(filter(lambda x: x.endswith(".png"), os.listdir(".")))
    mask_sizes = []
    for i, png_file in enumerate(png_files):
        mask_size = CalculateMaskSize(png_file)
        mask_sizes.append(mask_size)
        print("{0}/{1} {2}".format(i+1, len(png_files), mask_size))
    max_size = max(mask_sizes)
    level_size = int(round(max_size/level_count))
    levels = range(0, max_size, level_size)
    levels_with_counts = []
    for i in range(len(levels)-1):
        levels_with_counts.append((len(list(filter(lambda x: levels[i] < x <= levels[i+1], mask_sizes))), levels[i]))
    return levels_with_counts

def CalculateMaskSize(png_file):
    img = Image.open(png_file, mode='r') if png_file is not None else Image.new('L', TARGET_SIZE)
    img_array = np.asarray(img)
    unique, counts = np.unique(img_array, return_counts=True)
    result = dict(zip(unique, counts))
    return result[255] if 255 in result else 0
