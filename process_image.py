import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray




def show_image_info(image_path, slide):
    print ("Read WSI from %s with width: %d, height: %d" % (image_path,
                                                            slide.level_dimensions[0][0],
                                                            slide.level_dimensions[0][1]))
    for i in range(len(slide.level_dimensions)):
        print("Level %d, dimensions: %s downsample factor %d" % (i,
                                                                 slide.level_dimensions[i],
                                                                 slide.level_downsamples[i]))
    width, height = slide.level_dimensions[7]
    print(width, height)
    assert width * slide.level_downsamples[7] == slide.level_dimensions[0][0]
    assert height * slide.level_downsamples[7] == slide.level_dimensions[0][1]


# Read a region from the slide
# Return a numpy RBG array
def read_slide(slide, x, y, level, width, height, as_float=False):
    im = slide.read_region((x,y), level, (width, height))
    im = im.convert('RGB') # drop the alpha channel
    if as_float:
        im = np.asarray(im, dtype=np.float32)
    else:
        im = np.asarray(im)
    assert im.shape == (height, width, 3)
    return im


def find_tissue_pixels(image, intensity=0.8):
    im_gray = rgb2gray(image)
    assert im_gray.shape == (image.shape[0], image.shape[1])
    indices = np.where(im_gray <= intensity)
    return list(zip(indices[0], indices[1]))


def apply_mask(im, mask, color=(255,0,0)):
    masked = np.copy(im)
    for x,y in mask: masked[x][y] = color
    return masked


def show_image(img, figsize = (10,10), dpi=100, overlapping_img = None, title=None):
    fig = plt.figure(figsize=figsize, dpi=dpi)
    fig.canvas.set_window_title(title)
    plt.imshow(img)
    if(overlapping_img is not None):
        plt.imshow(overlapping_img, cmap='jet', alpha=0.5)  # Red regions contains cancer.
    plt.show()