import matplotlib.pyplot as plt
from openslide import open_slide, __library_version__ as openslide_version

from process_image import *

IMG_PATH = r'dataset/tumor_091.tif'
MASK_PATH = r'dataset/tumor_091_mask.tif'

slide = open_slide(IMG_PATH)
tumor_mask = open_slide(MASK_PATH)
slide_image = read_slide(slide,
                         x=0,
                         y=0,
                         level=5,
                         width=slide.level_dimensions[5][0],
                         height=slide.level_dimensions[5][1])

show_image_info(IMG_PATH, slide)
show_image_info(MASK_PATH, tumor_mask)
show_image(slide_image, title="Region from the fifth slide")




# Example: read the entire mask at the same zoom level
mask_image = read_slide(tumor_mask,
                        x=0,
                        y=0,
                        level=5,
                        width=slide.level_dimensions[5][0],
                        height=slide.level_dimensions[5][1])

# Note: mask contains R,G,B channels.
# The mask info is in the first channel only.
mask_image = mask_image[:, :, 0]

show_image(mask_image, title="Mask image region")

# Overlay image and mask

show_image(slide_image, overlapping_img=mask_image, title="Overlapped image and mask")
region = read_slide(tumor_mask, x=350 * 128, y=120 * 128, level=7, width=50, height=50)[:, :, 0]
show_image(region, title="Tumor region")


tissue_pixels = find_tissue_pixels(slide_image)
percent_tissue = len(tissue_pixels) / float(slide_image.shape[0] * slide_image.shape[1]) * 100
print ("%d tissue_pixels pixels (%.1f percent of the image)" % (len(tissue_pixels), percent_tissue))


tissue_regions = apply_mask(slide_image, tissue_pixels)
show_image(tissue_regions, title="Tissue regions")
show_image(tissue_regions, overlapping_img=mask_image, title="New overlapping of tissue regions and mask")
