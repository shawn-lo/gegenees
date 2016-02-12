import numpy as np
class Filters(object):
    def __init__(self):
        pass

    def fit(self, model, data):
        print(model)
        height, width = data.shape[:2]
        winHeight, winWidth = model.shape[:2]
        offVector = (int(winWidth/2), int(winHeight/2))

        tmp = np.zeros((height, width, 3), dtype='float32')
        # y, x - loop for every pixel in image
        for y in range(0, height):
            for x in range(0, width):
                # yWin, xWin - loop for pixels in filter window
                for yWin in range(-offVector[1], offVector[1]+1):
                    for xWin in range(-offVector[0], offVector[0]+1):
                        tempIntensity = [0,0,0]
                        xImInd = x + xWin
                        yImInd = y + yWin
                        xFilInd = xWin + offVector[0]
                        yFilInd = yWin + offVector[1]
                        # 8 conditions??? Any better method?
                        # left side, no corners
                        if xImInd < 0 and yImInd >= 0 and yImInd < height:
                            tempIntensity = data[yImInd][0]
                        # right side, no corners
                        elif xImInd >= width and yImInd >=0 and yImInd < height:
                            tempIntensity = data[yImInd][width-1]
                        # up side, no corners
                        elif yImInd < 0 and xImInd >=0 and xImInd < width:
                            tempIntensity = data[0][xImInd]
                        # bottom side, no corners
                        elif yImInd >= height and xImInd >=0 and xImInd < width:
                            tempIntensity = data[height-1][xImInd]
                        # up-left corner
                        elif xImInd < 0 and yImInd < 0:
                            tempIntensity = data[0][0]
                        # up-right corner
                        elif xImInd >= width and yImInd < 0:
                            tempIntensity = data[0][width-1]
                        # bottom-left corner
                        elif xImInd < 0 and yImInd >= height:
                            tempIntensity = data[height-1][0]
                        # bottom-right corner
                        elif xImInd >= width and yImInd >= height:
                            tempIntensity = data[height-1][width-1]
                        # inside of befor image
                        else:
                            tempIntensity = data[yImInd][xImInd]
#                        print(tempIntensity)
#                        print(model[yFilInd][xFilInd])
                        tmp[y][x][0] += tempIntensity[0] * model[yFilInd][xFilInd]
                        tmp[y][x][1] += tempIntensity[1] * model[yFilInd][xFilInd]
                        tmp[y][x][2] += tempIntensity[2] * model[yFilInd][xFilInd]
                        # use cut-off strategy
                        if tmp[y][x][0] > 255:
                            tmp[y][x][0] = 255
                        if tmp[y][x][1] > 255:
                            tmp[y][x][1] = 255
                        if tmp[y][x][2] > 255:
                            tmp[y][x][2] = 255
        result = tmp.astype(int)
        print(result)
        return result

