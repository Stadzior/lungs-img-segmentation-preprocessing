import numpy as np
from PIL import Image
from logHelper import ExecuteWithLogs
import os

def PerformPreprocessing(log_file_path):    
    for file in filter(lambda x: x.endswith(".raw"), os.listdir(".")):
        f = open(file, 'rb')
        img_str = f.read()

        isMask = "MM" in file

        # converting to a int8/int16 numpy array
        ct_image_as_vector = np.fromstring(img_str, dtype=np.int8) if isMask else np.fromstring(img_str, np.int16)

        #layering
        layer_dimensions = (512, 512)
        layer_size = layer_dimensions[0]*layer_dimensions[1]
        layers_count = int(len(ct_image_as_vector) / layer_size)
        ct_image_layered = np.reshape(ct_image_as_vector, (layers_count, layer_size))

        # get the image and plot it
        if isMask:
            for i, layer in enumerate(ct_image_layered):
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