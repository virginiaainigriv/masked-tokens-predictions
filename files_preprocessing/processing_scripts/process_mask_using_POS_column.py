import os
import pandas as pd
import re
import random

'''
Globals to be used througout the script. Grouped here for simplicity reasons
'''
MASK_WORD = '[MASK]'
LEMMA_REGEX = re.compile('word+\/+[0-9]+\/lemma+\/@_entry')
POS_REGEX = re.compile('word+\/+[0-9]+\/lemma+\/@_POS')

SOURCE = '../files_source/sampled_files'
DESTINATION = '../files_destination/sampled_files_masked'

STRIPPED_FILES = os.listdir(SOURCE)


class Masking:
    def __init__(self, source_path, output_name):
        self.file = {
        'source_path': source_path,
        'output_name': output_name,
        'words': {
            'all': {
                'count': 0,
                'percentage': 0,
            },
            'nouns': {
                'count': 0,
                'percentage': 0,
            },
            'verbs': {
                'count': 0,
                'percentage': 0,
            },
            'adjectives': {
                'count': 0,
                'percentage': 0,
            }
        }
    }

        self.initialise_word_count()
        self.initialise_word_percentage()


    def initialise_word_count(self):
        #count the actual number of words in the dataframe excluding NAN values to mask effectively 15% of words

        df = pd.read_csv(self.file['source_path'])
        
        base = self.file['words']

        # usign part of speach tag column to make splitting among word categories easier
        # loop through each POS column of the dataframe and each row to count how many words of each category
        for col in df.columns:
            if POS_REGEX.match(col):
                base['all']['count'] = base['all']['count'] + df[col].count()

                for i in range(df.shape[0]):
                    if df[col].loc[i] == "noun":
                        base['nouns']['count'] = base['nouns']['count'] + 1
                    if df[col].loc[i] == "verb":
                        base['verbs']['count'] = base['verbs']['count'] + 1
                    if df[col].loc[i] == "adjective":
                        base['adjectives']['count'] = base['adjectives']['count'] + 1    
        

    def initialise_word_percentage(self):
        # calculate 15% of each word category.
        # 15% chosen because balanced number in masking algorithms

        base = self.file['words']

        base['all']['percentage'] = round(base['all']['count'] * 0.15),
        base['nouns']['percentage'] = round(base['nouns']['count'] * 0.15),
        base['verbs']['percentage'] = round(base['verbs']['count'] * 0.15),
        base['adjectives']['percentage'] = round(base['adjectives']['count'] * 0.15),


    def instruct_word_masking(self, df):
               
        print(self.prepare_mask_all_types_of_words(df, MASK_WORD))


    def get_largest_column_index(self, df, row):
        # find the largest possible index of column for each row of the dataframe
        # only necessary to look trhough one kind of columns (lemma entry) because it's not a sparse dataframe
        # 1 lemma entry = 1 beta code = 1 POS 

        large_column = 0
        

        for col in df.columns:
            
            if LEMMA_REGEX.match(col) != None:
                                
                # cells with nan values are floats, so check if cell is string
                if isinstance(row[col], str):
                    large_column = int(col[5:(len(col)-14)])
                                                
        return large_column

    def prepare_mask_all_types_of_words(self, df, mask_word):
        
        masked_words = 0
        
        # loop over every row in the dataframe
        for i, row in df.iterrows():
            
            large_col = self.get_largest_column_index(df, row)
            
            if large_col == 0:
                break     
            
            '''
            EDIT THE ALLOWED_POS TO FILTER MASKING WORDS
            
            ALL POSSIBLE CATEGORIES:
            noun
            pronoun
            adjective
            adverb
            verb
            article
            conjunction
            particle
            proper
            preposition
            interjection
            '''
            allowed_POS = ['noun', 'pronoun']
            
            col_number = random.randint(0, large_col) # get two random numbers to select random cell
            
            attempt = 0
            while not row[f'word/{col_number}/lemma/@_POS'] in allowed_POS:
               
                col_number = random.randint(0, large_col) # get two random numbers to select random cell
                attempt +=1
                
                if attempt > 5:
                    break
    
                                           
            row[f'word/{col_number}/lemma/@_entry'] = mask_word
            masked_words += 1
            
        precentage = (masked_words / self.file['words']['all']['count'])*100
        print(f"{self.file['output_name']} masked {precentage}% all words")
        
        self.to_text_file(df, 'mask')   
                  

          
    def to_text_file(self, df, specification_name):
        columns = [] 
        for col in df.columns:  # use only columns containing greek words in greek characters
            if LEMMA_REGEX.match(col) != None:
                columns.append(col)
        df1 = df[columns]

        output_name = self.file['output_name']

        df1.to_csv(f'{DESTINATION}/{output_name}_{specification_name}.txt', sep=' ', index=False, header=False)


erroring_files = []

for f in STRIPPED_FILES:

    source_path = os.path.join(SOURCE, f) # source of the half processed file
    output_name = os.path.splitext(f)[0] # name of file without extension, to be used when outputting csv masked file

    file = Masking(source_path, output_name)

    df = pd.read_csv(source_path)

    try:
        file.instruct_word_masking(df)
        
    except Exception as e:
        erroring_files.append(output_name)
        print(e)
    
     
    
print(erroring_files)