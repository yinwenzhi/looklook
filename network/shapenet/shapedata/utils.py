# author: Justus Schock (justus.schock@rwth-aachen.de)

import os

IMG_EXTENSIONS_2D = [
    ".png", ".PNG", ".jpg", ".JPG"
]

LMK_EXTENSIONS = [
    ".txt", ".TXT", ".ljson", ".LJSON", ".pts", ".PTS"
]



def is_image_file(filename):
    """
    Helper Function to determine whether a file is an image file or not
    :param filename: the filename containing a possible image
    :return: True if file is image file, False otherwise
    """
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS_2D)


def is_landmark_file(filename):
    return any(filename.endswith(extension) for extension in LMK_EXTENSIONS)


def make_dataset(dir):
    """
    Helper Function to make a dataset containing all images in a certain
    directory
    :param dir: the directory containing the dataset
    :return: images: list of image paths
    """
    images = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir

    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname) and any(
                    [os.path.isfile(os.path.join(root,
                                                 fname.rsplit(".", 1)[0] + ext)
                                    ) for ext in LMK_EXTENSIONS]):
                path = os.path.join(root, fname)
                images.append(path)



    return images