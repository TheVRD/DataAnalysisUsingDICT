from csv import reader as csvreader
import collections

medalCSV = "medals.csv"
atheleteCSV = "athletes.csv"

#reading csv file containing medals data
with open(medalCSV, 'r') as fp:
    reader = csvreader(fp)
    medals = list(reader)

#reading csv file containing atheletes data
with open(atheleteCSV, 'r', encoding='utf-8') as fp:
    reader = csvreader(fp)
    athletes = list(reader)

#creating dict containing medal details
medal_details = {
    "raw_data": medals,
    "columns": medals[0],
    "data": medals[1:]
    }

#creating dict containg atheletes data
atheletes_details = {
    "raw_data":athletes,
    "columns":athletes[0],
    "data":athletes[1:]
    }
#adding descriptions to both medals and athelete data
medal_details["description"] = "contains data about different medal winners and their sports"
atheletes_details["description"] = "contains data about different atheletes"

#creating a dict combining both the above dictionaries 
dataset = {
    "medals": medal_details,
    "atheletes": atheletes_details
    }
def maximaAndMinima(tempDict):
    maxvalue, maxkey = 0,'a'
    for key,value in tempDict.items():
            if value>maxvalue:
                maxvalue = value
                maxkey = key
    return (maxkey,maxvalue)

resultLST = []
outresultLST = []

