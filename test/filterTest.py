from ..filters.gaussian_filter import GaussianFilter
import numpy as np
from scipy import ndimage
import scipy
from PIL import Image

if __name__ == '__main__':
    g = GaussianFilter(1)
    im = np.array(Image.open('/Users/Shawn/Desktop/Rainbow-panda-laser.jpg'))
    res = g.fit(im)
    scipy.misc.imsave('/Users/Shawn/Desktop/g.jpg', res)

