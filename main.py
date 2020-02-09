import xlrd
import pandas as pd
from itertools import islice
from openpyxl import load_workbook
from Stats import Stats

workbook = xlrd.open_workbook("Music Data.xlsx")
sheet = workbook.sheet_by_index(0)

allBands = [ str(sheet.cell_value(i, 0)) for i in range(sheet.nrows) ]
allAlbums = [ str(sheet.cell_value(i, 1)) for i in range(sheet.nrows) ]
allGenres = [ str(sheet.cell_value(i, 2)) for i in range(sheet.nrows) ]
allYears = [ str(sheet.cell_value(i, 3)) for i in range(sheet.nrows) ]
allLengths = [ str(sheet.cell_value(i, 4)) for i in range(sheet.nrows) ]
allLabels = [ str(sheet.cell_value(i, 5)) for i in range(sheet.nrows) ]
allCountries = [ str(sheet.cell_value(i, 6)) for i in range(sheet.nrows)]

print(allLengths)
allStats = Stats()

dictBands = allStats.setStats(allBands)
dictGenres = allStats.setStats(allGenres)
dictYears = allStats.setStats(allYears)
dictLabels = allStats.setStats(allLabels)
dictCountries = allStats.setStats(allCountries)

dictCountries.pop("-", None)

allStats.setLengthStats(allLengths, allAlbums)

book = load_workbook("Music Data.xlsx")

bandsSheet = book["Albums from Bands"]
genresSheet = book["Genre"]
yearSheet = book["Year"]
labelsSheet = book["Record Label"]
countrySheet = book["Country of Origin"]

print(f"The average length of the albums I've heard is {allStats.getAverageLength()}.")
print(f"The shortest album I've heard anything from is {allStats.getShorestAlbumName()} with a runtime of {allStats.getShortestAlbum()}.")
print(f"The longest album I've heard anything from is {allStats.getLongestAlbumName} with a runtime of {allStats.getLongestAlbum()}.")

print("Please check out the excel sheet for more info!")

book.save("Movie Data.xlsx")
book.close()