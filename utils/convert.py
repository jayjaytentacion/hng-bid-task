import csv
import json
import hashlib


       

def convert_hash(csvfilepath):
    '''
    This function takes in @csvfilepath as a parameter
    and goes through each line and convert them to json and sore them
    in files,hashes them and return the hashes as a list
    '''

    #sample chip007 format
    data = {
          "format": "CHIP-0007",
            "name": "",
            "description": "",
            "minting_tool": "TEAM GRIT",
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

    
    #list to store hashes
    hashes = []


    #opens the csv file 
    with open(csvfilepath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
    

         
        # Convert each row into a dictionary
        # and add it to data
        
        for rows in csvReader:
                     
            data['collection']['id'] = rows["UUID"]
            # data["minting_tool"] = rows['TEAM NAMES']
            data["series_number"] = rows['Series Number']
            data["description"] = rows['Description']
            data["name"] = rows['Filename']
            data["attributes"][0]['value'] = rows['Gender']

            

            

            #get name of nft to save as output name
            name = rows['Filename']
            jsonFilePath='json/'+ name + '.json'

            #creates a json file with name from the nft
            with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))
            #hashes json after file has been created 
            hashes.append(hashlib.sha256(open(jsonFilePath, 'rb').read()).hexdigest())
            break

        print('Json files generated succesfully @./json Directory')    
        
        #return dictionary of hashes
        return hashes
               
           
        
            
               
                 

