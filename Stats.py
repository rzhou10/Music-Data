from itertools import islice
import sys

class Stats():
    averageLength = ""
    longestAlbum = 0
    longestAlbumName = ""
    longestAlbumBand = ""
    shortestAlbum = sys.maxsize
    shortestAlbumName = ""
    shortestAlbumBand = ""
    
    def setStats(self, statList):
        statsAsDict = {}

        for i in islice(statList, 1, None):
            if i not in statsAsDict:
                statsAsDict[i] = 0
            statsAsDict[i] += 1
        
        return statsAsDict
    
    def setLengthStats(self, lengthList, titleList, bandList):
        # the time will be calculated in seconds for easier computations
        totalTime = 0

        noFirst = list(islice(lengthList, 1, None))

        for i in range(len(noFirst)):
            timeParts = [int(s) for s in noFirst[i].split(':')]
            lengthInSec = (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]

            if lengthInSec > self.longestAlbum:
                self.longestAlbum = lengthInSec
                self.longestAlbumName = titleList[i + 1]
                self.longestAlbumBand = bandList[i + 1]
            if lengthInSec < self.shortestAlbum:
                self.shortestAlbum = lengthInSec
                self.shortestAlbumName = titleList[i + 1]
                self.shortestAlbumBand = bandList[i + 1]
            totalTime += lengthInSec

        averageInSec = int(totalTime / len(lengthList))
        hoursMin, sec = divmod(averageInSec, 60)
        hour, minute = divmod(hoursMin, 60)
        hourStr = f"{hour}"

        if 0 <= hour <= 9:
            hourStr = "0" + str(hour)

        self.averageLength = f"{hourStr}:{minute}:{sec}"
    
    def getAverageLength(self):
        return self.averageLength
    
    def getLongestAlbum(self):
        hoursMin, sec = divmod(self.longestAlbum, 60)
        hour, minute = divmod(hoursMin, 60)
        hourStr = f"{hour}"

        if 0 <= hour <= 9:
            hourStr = "0" + str(hour)
            
        return f"{hourStr}:{minute}:{sec}"
    
    def getLongestAlbumName(self):
        return self.longestAlbumName
    
    def getLongestAlbumBand(self):
        return self.longestAlbumBand
    
    def getShortestAlbum(self):
        hoursMin, sec = divmod(self.shortestAlbum, 60)
        hour, minute = divmod(hoursMin, 60)
        hourStr = f"{hour}"

        if 0 <= hour <= 9:
            hourStr = "0" + str(hour)

        return f"{hourStr}:{minute}:{sec}"
    
    def getShorestAlbumName(self):
        return self.shortestAlbumName
    
    def getShortestAlbumband(self):
        return self.shortestAlbumBand