import numpy as np
from .filters import Filters
class SobelFilter(Filters):

    def __init__(self, threshold, axis):
        self.threshold = threshold
        self.axis = axis

    def fit(self, data):
        model = self.constructModel(self.threshold, self.axis)
        return super().fit(model, data)

    def constructModel(self, threshold, axis):
        if axis == 0:
            sFilter = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        elif axis == 1:
            sFilter = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
        return sFilter
