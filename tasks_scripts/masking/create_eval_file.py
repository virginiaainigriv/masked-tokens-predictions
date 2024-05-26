import os

# Set the path to the folder containing the files
folder_path = '../../files_preprocessing/files_destination/sampled_files_masked/masked_noun_pronoun'

# Create a new file to write the summary to
new_file_path = '../../files_preprocessing/files_destination/sampled_files_masked/sample_summary_noun_pronoun.txt'

with open(new_file_path, 'w') as f_out:
    
    # Loop over all files in the folder
    for filename in os.listdir(folder_path):

        # Only process text files
        if filename.endswith('.txt'):

            # Read the first 15 lines of the original file and write them to the summary file
            with open(os.path.join(folder_path, filename), 'r') as f_in:
                for i, line in enumerate(f_in):
                    if i == 30:
                        break
                    f_out.write(line)
            f_out.write('\n')
