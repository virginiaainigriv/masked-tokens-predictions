import os
import pandas as pd
import re


SOURCE = '../files_source/diorisis_csv'
DESTINATION = '../files_source/half_processed_files'

# Strips all files of unnecessary information
# All csv files will contain just three types of columns: beta code values, lemma entry values and part of speach tagging
def strip_csv_files(file, file_name):
    df = pd.read_csv(file)

    beta_code_regex = re.compile('word+\/+[0-9]+\/@_form')
    lemma_entry_regex = re.compile('word+\/+[0-9]+\/lemma+\/@_entry')
    pos_regex = re.compile('word+\/+[0-9]+\/lemma+\/@_POS')

    for col in df.columns:
        if beta_code_regex.match(col) == None and lemma_entry_regex.match(col) == None and pos_regex.match(col) == None:
            df = df.drop(col, axis=1)

    df.to_csv(f'{DESTINATION}/{file_name}.csv', index=False)

    return (f'Completed stripping for {file_name}')


# collect all files to be processed, stored in unprocessed_files folder

FILES = os.listdir(SOURCE)


for file in FILES:
    # used to construct the new file name for the stripped csv file
    file_name= os.path.splitext(file)[0]
    file_path = os.path.join(SOURCE, file)
    
    print(strip_csv_files(file_path, file_name))