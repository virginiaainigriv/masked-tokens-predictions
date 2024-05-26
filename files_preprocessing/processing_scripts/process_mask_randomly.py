import random
import os

# Set the source and destination directories
SOURCE = '../files_source/modern_greek'
DESTINATION = '../files_destination/modern_greek'

# Get a list of all files in the source directory
STRIPPED_FILES = os.listdir(SOURCE)

# Function to save a list of lines to a text file
def save_lines(lines, output_path):
    with open(output_path, 'w') as f:
        f.writelines(lines)

# List to store the names of files that encountered errors during processing
erroring_files = []

# Process each file in the source directory
for f in STRIPPED_FILES:
    source_path = os.path.join(SOURCE, f) # source of the half processed file
    output_name = os.path.splitext(f)[0] + '_masked.txt' # output filename with "_masked" suffix
    
    # Load the corpus from the source file
    with open(source_path, 'r') as f:
        corpus = f.readlines()

    try:
        # Mask one random word per sentence
        masked_corpus = []
        for sentence in corpus:
            words = sentence.split()
            if len(words) > 2: # Ensure the sentence has more than one word
                # Choose a random word to mask (excluding the first and last words)
                mask_index = random.randint(1, len(words)-2)
                words[mask_index] = '[MASK]'
                masked_sentence = ' '.join(words)
                masked_corpus.append(masked_sentence + '\n')
            else:
                masked_corpus.append(sentence) # Don't mask single-word sentences
        
        # Save the masked corpus to a new file in the destination directory
        output_path = os.path.join(DESTINATION, output_name)
        save_lines(masked_corpus, output_path)
    except Exception as e:
        erroring_files.append(output_name)
        print('An error occurred while processing file:', e)

# Print the names of files that encountered errors during processing
if erroring_files:
    print('The following files encountered errors during processing:')
    for f in erroring_files:
        print(f)    
