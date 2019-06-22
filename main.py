import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import skimage.io as io

os.chdir("./data")

#uint8
newMin = 0
newMax = 255 
newRange = (newMax - newMin)  

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
    for i, layer in enumerate(ct_image_layered):
        #layer.byteswap(inplace=True)        
        #Normalize function
        if (not isMask):
            oldMin = layer.min()
            oldMax = layer.max()
            oldRange = (oldMax - oldMin) 
            normalize = lambda x: int((((x - oldMin) * newRange) / oldRange) + newMin)
            npNormalize = np.vectorize(normalize)
            layer = npNormalize(layer).astype(np.int8)
        layer = np.reshape(layer, (512, 512))
        image = Image.fromarray(layer, "L") 
        image.save("{0}_{1}.png".format(file, i), "PNG")
