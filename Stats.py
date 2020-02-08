from itertools import islice
import sys

class Stats():
    averageLength = ""
    longestAlbum = 0
    longestAlbumName = ""
    shortestAlbum = sys.maxsize
    shortestAlbumName = ""
    
    def setStats(self, statList):
        statsAsDict = {}

        for i in islice(statList, 1, None):
            if i not in statsAsDict:
                statsAsDict[i] = 0
            statsAsDict[i] += 1
        
        return statsAsDict
    
    def setLengthStats(self, lengthList, titleList):
        # the time will be calculated in seconds for easier computations
        totalTime = 0

        noFirst = list(islice(lengthList, 1, None))

        for i in range(len(noFirst)):
            timeParts = [int(s) for s in noFirst[i].split(':')]
            lengthInSec = (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]

            if lengthInSec > self.longestAlbum:
                self.longestAlbum = lengthInSec
                self.longestAlbumName = titleList[i + 1]
            if lengthInSec < self.shortestAlbum:
                self.shortestAlbum = lengthInSec
                self.shortestAlbumName = titleList[i + 1]

            totalTime += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
        averageInSec = totalTime / len(lengthList)
        totalSecs, sec = divmod(averageInSec, 60)
        hour, minute = divmod(totalSecs, 60)
        self.averageLength = f"{hour}:{minute}:{sec}"
    
    def getAverageLength(self):
        return self.averageLength
    
    def getLongestAlbum(self):
        return self.longestAlbum
    
    def getLongestAlbumName(self):
        return self.longestAlbumName
    
    def getShortestAlbum(self):
        return self.shortestAlbum
    
    def getShorestAlbumName(self):
        return self.shortestAlbumName