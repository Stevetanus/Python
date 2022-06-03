import os
import csv
os.chdir('.\Ch16-Working_with_csv_json')
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleDate = list(exampleReader)
exampleDate
exampleDate[0][0]
exampleDate[0][1]
exampleDate[6][1]
# for loop in large data file
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
# write csv
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415926, 4])
outputFile.close()
# delimiter分隔符號 lineterminator行尾終止符號
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()
# DictReader DictWriter
exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])
# DictReader set rownames
exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name', 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
# DictWriter write csv
outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'],delimiter='\t')
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'})
outputFile.close()
# json
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
# dumps json to python value
pythonValue = {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
stringOfJsonData