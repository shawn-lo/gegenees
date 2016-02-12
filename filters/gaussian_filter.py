import numpy as np
from .filters import Filters
class GaussianFilter(Filters):

    def __init__(self, sigma=1):
        self.sigma = sigma

    def fit(self, data):
        model = self.constructModel(self.sigma)
        return super().fit(model, data)

    def constructModel(self, sigma):
        winSize = sigma*6 - 1
        # construct gaussian filter
        gFilter = np.zeros((winSize, winSize))
        # translate, (offX, offY)
        offVector = (int(winSize/2), int(winSize/2))

        scale = 1/(2*np.pi*sigma**2)
        precision = 0
        for yIndex in range(0, winSize):
            y = yIndex - offVector[1]
            for xIndex in range(0, winSize):
                x = xIndex - offVector[0]
                temp = -(x**2+y**2)/(2*sigma**2)
                gFilter[yIndex][xIndex] = scale*np.exp(temp)
                precision += gFilter[yIndex][xIndex]
        return gFilter
