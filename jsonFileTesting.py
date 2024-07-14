import json

jsonFile = open("trancribedData.json")
fileData = json.load(jsonFile)
print(fileData["results"]["channels"][0]["alternatives"][0]["transcript"])
filedata1 = fileData["results"]["channels"]
print(filedata1[0]["alternatives"][0]["transcript"])
