from utils.convert import convert_csv
from utils.hash import hash
from utils.append import append

csvFilePath = "csv\\test.csv"

jsonfile=convert_csv(csvFilePath)

hashing=hash(jsonfile) 

append(hashing,csvFilePath)  




