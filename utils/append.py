from csv import writer
from csv import reader




def append(hash, file):
    num = 1

    name = file.split('.')
    # Second split using separator '/'
    outfile = name[0].split('/')
    outfile = name[0].split('\\')
    outfile='csv/'+ 'updated' + outfile[-1] + '.csv'
   
    # Open the input_file in read mode and output_file in write mode
    with open(file, 'r') as read_obj, \
            open(  outfile , 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        line_num = csv_reader.line_num
   
 
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Append the default text in the row / list
            if (line_num == 0):
              
                pass
                
            else:
                    

             row.append(hash)
            # Add the updated row / list to the output file
            csv_writer.writerow(row)
            line_num+=1

       