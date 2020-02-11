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
print(f"The longest album I've heard anything from is {allStats.getLongestAlbumName()} with a runtime of {allStats.getLongestAlbum()}.")

print("Please check out the excel sheet for more info!")

bandData = pd.DataFrame(
    {
        "Band": [ key for key, value in dictBands.items() ],
        "Count": [ value for key, value in dictBands.items() ],
    }
)

genreData = pd.DataFrame(
    {
        "Genre": [ key for key, value in dictGenres.items() ],
        "Count": [ value for key, value in dictGenres.items() ],
    }
)

yearData = pd.DataFrame(
    {
        "Year": [ key for key, value in dictYears.items() ],
        "Count": [ value for key, value in dictYears.items() ],
    }
)

labelData = pd.DataFrame(
    {
        "Label": [ key for key, value in dictLabels.items() ],
        "Count": [ value for key, value in dictLabels.items() ],
    }
)

countryData = pd.DataFrame(
    {
        "Country": [ key for key, value in dictCountries.items() ],
        "Count": [ value for key, value in dictCountries.items() ],
    }
)

for index, row in bandData.iterrows():
    band = f"A{index + 1}"
    count = f"B{index + 1}"
    bandsSheet[f"A{index + 1}"] = row[0]
    bandsSheet[count] = row[1]

for index, row in genreData.iterrows():
    genre = f"A{index + 1}"
    count = f"B{index + 1}"
    genresSheet[genre] = row[0]
    genresSheet[count] = row[1]

for index, row in yearData.iterrows():
    year = f"A{index + 1}"
    count = f"B{index + 1}"
    yearSheet[year] = row[0]
    yearSheet[count] = row[1]

for index, row in labelData.iterrows():
    label = f"A{index + 1}"
    count = f"B{index + 1}"
    labelsSheet[label] = row[0]
    labelsSheet[count] = row[1]

for index, row in countryData.iterrows():
    country = f"A{index + 1}"
    count = f"B{index + 1}"
    countrySheet[country] = row[0]
    countrySheet[count] = row[1]

book.save("Music Data.xlsx")
book.close()