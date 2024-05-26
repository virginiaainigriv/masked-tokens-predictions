import os

base = '../files_destination'

source = f"{base}/diorisis_raw_files" 
destination = f"{base}/training_files" 

files = os.listdir(source)
# Count the number of files in the directory
num_files = len(files)

def merge_files(source, destination_file):
    
    with open(destination_file, "w") as outfile:
        
        for filename in files:
            
            if filename.endswith(".txt"):
                
                with open(os.path.join(source, filename), "r") as infile:
                    outfile.write(infile.read())
                    
                print('Added file ', filename)
                    
merge_files(source, f'{destination}/all_diorisis.txt')

