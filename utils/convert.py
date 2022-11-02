import csv
import json




def convert_csv(csvfilepath,):
    name = csvfilepath.split('.')
    # Second split using separator '/'
    file = name[0].split('/')
    file = name[0].split('\\')
    
    # Printing the filename without extension
    jsonFilePath='json/'+ file[-1] + '.json'
    


    data = {
         
    }
    dat = []

     # Open a csv reader called DictReader
    with open(csvfilepath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            data['format']=  "CHIP-0007"
            data['collection'] = rows
            dat.append(data)
         


            
 
    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(dat, indent=4))
         
    return jsonFilePath     

