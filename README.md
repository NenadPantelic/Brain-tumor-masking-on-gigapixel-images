# Brain-tumor-masking-on-gigapixel-images

Dependencies:

- scikit
- matplotlib
- numpy
- openslide

Openslide installation instructions:
Linux:
- apt-get install openslide-tools
- pip install openslide-python
Windows:

After installation of python openslide library (pip3 install openslide-python), you need to download original Openslide library:
https://openslide.org/download/ and choose appropriate windows binary file (2017-11-22	64-bit is my (tested) version).
After download, extract openslide folder and:
1) The last step is to set system environment variable - set openslide bin folder path (path\to\your\extraction\folder\openslide-win64-20171122\bin
2) Or copy all the content from the bin folder and paste it to Python env path (you can get this folder with the following Python code:
import sys
print (sys.path) - it should like something like this:
C:\Users\yourusername\AppData\Local\Programs\Python\Python35 and paste there all the dlls from bin folder

Dataset:
Complete dataset used in this project can be found at this link:
https://camelyon17.grand-challenge.org/Data/

Gigapixel images are converted into an appropriated format with ASAP. Here you can found some of formatted images:
https://drive.google.com/drive/folders/1rwWL8zU9v0M27BtQKI52bF6bVLW82RL5

In this project we used 91st image example. So you can download it from the link above and put it in dataset directory, so that path looks like:
1) dataset/tumor_091.tif
2) dataset/tumor_091_mask.tif

If you wan't to convert other images you must download ASAP:
https://github.com/computationalpathologygroup/ASAP/releases
