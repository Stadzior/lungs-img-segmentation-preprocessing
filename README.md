# Lungs image segmentation Preprocessing
Repo created as a part of master degree thesis:<br />
"Segmentation of limited opacity CT lung images with the use of convolutional neural networks".<br />
Preprocessing part of the solution, it converts raw files into set of png files representing mhd/raw layers. <br />
The following project was tested on Python 3.6.8 64bit on Windows 10.
<b>Output files:</b> 

## Quickstart:  
1. Prepare input files in the following format: <b>16bit .raw file</b> with CT images OR <b>1bit .raw file</b> with binary mask (to indicate that this is a mask you need to add "MM" in the file name).
2. Copy files to `.\data`.
3. Run [main.py](main.py).
4. The progress should be visible on output window.
5. After the run termination you should find your <b>set of 8bit .png files</b> in `.\data`.

A full recording of the run can be found in [log.txt](data\log.txt).<br />
<b>CalculateMaskSize</b> in [preprocessingHelper.py](preprocessingHelper.py) can be used to calculate surface area of a lungs on a certain layer according to binary mask (png file).<br />
<b>CalculateMaskSizeLevels</b> in [preprocessingHelper.py](preprocessingHelper.py) can be used to split output .png files into ranges of masks of certain calculated surface area (useful in you want to distinguish boundary lung areas).