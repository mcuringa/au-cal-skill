import csv
import json

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}

    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        #convert each csv row into python dict
        for row in csvReader:
            #add this python dict to json array
            data[row["key"]] = row

    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(data, indent=2)
        jsonf.write(jsonString)

csv_to_json("fall.csv", "fall.json")
csv_to_json("spring.csv", "spring.json")
