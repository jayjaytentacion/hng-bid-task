import csv
import json
import hashlib
from typing import Final


       

def convert_csv(csvfilepath,):
   
    data = {
          "format": "CHIP-0007",
            "name": "",
            "description": "",
            "minting_tool": "",
            "sensitive_content": False,
            "series_number": "",
            "series_total": 420,
            "attributes": [
                {
                    "trait_type": "gender",
                    "value": ''
                }
            ],
            "collection": {
                "name": "Zuri NFT tickets for free lunch",
                "id": "",
                "attributes": [
                    {
                        "type": "description",
                        "value": "Rewards for accomplishments during HNGi9"
                    }
                ]
            },
        }

    
    
    hashes = []

     # Open a csv reader called DictReader
    with open(csvfilepath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary
        # and add it to data
        
        for rows in csvReader:
          
           
            data['collection']['id'] = rows["UUID"]
            data["minting_tool"] = rows['TEAM NAMES']
            data["series_number"] = rows['Series Number']
            data["description"] = rows['Description']
            data["name"] = rows['Filename']

            

            
            name = rows['Filename']
            jsonFilePath='json/'+ name + '.json'
         
            with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))
       
            hashes.append(hashlib.sha256(open(jsonFilePath, 'rb').read()).hexdigest())
            
        
        return hashes
               
           
        
            
               
                 

