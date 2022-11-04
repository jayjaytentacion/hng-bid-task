from utils.convert import convert_csv
from utils.append import append
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, required=True)
args = parser.parse_args()

csvFilePath = args.f


if (csvFilePath.endswith(".csv")):
        if os.path.exists(csvFilePath) == False:
            raise Exception('File does not exist')
        else:    
            if os.stat(csvFilePath).st_size == 0:
                raise Exception('File is empty')
                
                




        hashlist = convert_csv(csvFilePath)

        append(hashlist,csvFilePath)
else:
    raise Exception('invalid file format')        




  




