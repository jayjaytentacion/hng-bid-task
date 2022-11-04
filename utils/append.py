from csv import writer
from csv import reader




def append(hash,file):
    '''
    appends hashes to new row in csvfilepath
    '''

    #get name of csvfile
    name = file.split('.')
    outfile = name[0].split('/')
    outfile = name[0].split('\\')
    outfile= outfile[-1] + '.output'+ '.csv'
   
    # Open the input_file in read mode and output_file in write mode
    with open(file, 'r') as read_obj, \
            open(  outfile , 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        
        #get current line number 
        line_num = csv_reader.line_num
   
 
        # Read each row of the input csv file as list
        for row in csv_reader:
            # if line_num is zero append heading hash
            if (line_num == 0):
              
                row.append('hash')
                
            else:
                # append corresponding hash to line in csv
                row.append(hash[line_num - 1])
            # Add the updated row / list to the output file
            csv_writer.writerow(row)
            line_num+=1
    print('Csv File generated succesfully @'+outfile)        

       