from utils.convert import convert_csv
from utils.append import append

csvFilePath = "csv\\omo.csv"

hashlist = convert_csv(csvFilePath)

append(hashlist,csvFilePath)




  




