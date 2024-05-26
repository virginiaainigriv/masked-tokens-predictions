import os
import pandas as pd
import re

LEMMA_REGEX = re.compile('word+\/+[0-9]+\/lemma+\/@_entry')
SOURCE = '../files_source/half_processed_files'
DESTINATION = '../files_destination/raw_files'


def to_text_file(df, destination_folder, specification_name):
        columns = [] 
        for col in df.columns:  # use only columns containing greek words in greek characters
            if LEMMA_REGEX.match(col) != None:
                columns.append(col)
        df1 = df[columns]

        '''        
        dataframe outputted as:
            row -> row of text file
            column -> space separated values 
            header columns -> not printed
            index column -> not printed
        '''
        df1.to_csv(f'{destination_folder}/{output_name}_{specification_name}.txt', sep=' ', index=False, header=False)
        
        
stripped_files = os.listdir(SOURCE)

for f in stripped_files:
    
    print(f)

    source_path = os.path.join(SOURCE, f) # source of the half processed file
    output_name = os.path.splitext(f)[0] # name of file without extension, to be used when outputting csv masked file

    df = pd.read_csv(source_path)

    specification_name = ''
    to_text_file(df, DESTINATION, specification_name)

