# Lungs image segmentation Preprocessing
Preprocessing part of the solution, it converts raw files into set of png files representing mhd/raw layers. <br />
If you already have png files to work on just skip to [lungs-img-segmentation-unet](https://github.com/Stadzior/lungs-img-segmentation-unet) repo.<br />
The following project was tested on Python 3.6.8 64bit on Windows 10.

![title image](lungs-img-segmentation-preprocessing2.png)
## Quickstart:  
1. Prepare input files in the following format: <b>16bit .raw file</b> with CT images OR <b>1bit .raw file</b> with binary masks (to indicate that this is a mask you need to add "MM" in the file name).
2. Copy files to `.\data`.
3. Run [main.py](main.py).
4. The progress should be visible on output window.
5. After the run termination you should find your <b>set of 8bit .png files</b> in `.\data`.

A full recording of the run can be found in [log.txt](data\log.txt).<br />
<b>CalculateMaskSize</b> in [preprocessingHelper.py](preprocessingHelper.py) can be used to calculate surface area of a lungs on a certain layer according to binary mask (png file).<br />
<b>CalculateMaskSizeLevels</b> in [preprocessingHelper.py](preprocessingHelper.py) can be used to split output .png files into ranges of masks of certain calculated surface area (useful in you want to distinguish boundary lung areas).

## DISCLAIMER
Solution created as a part of my master degree thesis. If you want to use any part of those three solutions please add a reference to the following:<br />
<i>Kamil Stadryniak, "Segmentation of limited opacity CT lung images with the use of convolutional neural networks", Lodz University of Technology, 2019</i><br />

Another parts of the solution can be found here:<br />
[lungs-img-segmentation-unet](https://github.com/Stadzior/lungs-img-segmentation-unet)<br />
[lungs-img-segmentation-postprocessing](https://github.com/Stadzior/lungs-img-segmentation-postprocessing)

Examples included in `.\data` are a small part of larger dataset gathered by Centre de Recherche en Neurosciences de Lyon in cooperation with Université Claude Bernard Lyon 1, INSA, Centre de Recherche en Acquisition et Traitement de l'Image pour la Santé.

I've got the permission to publish just enough of them to make a working example thus they cannot be used in any kind of research or commercial solution without proper permission.
