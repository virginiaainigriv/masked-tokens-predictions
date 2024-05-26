# Understanding the effect of language distance in machine learning  transfer in natural language processing 

## Introduction

This folder contains processing and testing scripts that were used to draw the conclusions expressed and detailed in the associated paper and it is meant to be viewed in accordance to the apsects detailed in the study.

#

## Description of components

The project composes of two main folders:

> **`files_processing`**
which comprehends all the scripts to process the selected data and comprehends folders containing the outputs of all the processing. 

> **`project_tasks`** 
which comprehends all the script that make use of the processed data to draw conclusions and comprehends the files where outputs and conclusions can be found. 

### `files_processing`

- **`file_destination`** 

    - `diorisis_raw_files` all diorisis files stripped of all columns turned in txt just by concatenating lemma entry columns. used to prepare training data for fine tuning
    - `fine_tune_training_data` concatenated versions of selected diorisis_raw_files
    - `masked_files` all diorisis files masked for random word
    - `modern_greek` EU Parliament regulation files masked randomly
    - `sampled_files_clustering` chosen sample files in txt format concatenated lemma entry
    - `sampled_files_masked`  cchosen sample files in txt format concatenated lemma entry with mask token and collated 30 lines files for random and noun-pronoun analysis

_

- **`files_source`** contains files and product of the clustering task 
    - `diorisis_csv` all diorisis files converted from xml to csv, no data processing done
    - `half_processed_files` all diorisis files converted from xml to csv, removed all columns but data entry and POS tag
    - `modern_greek` EU Parliament regulation files txt format
    - `sampled_files` sampled files (see paper) converted from xml to csv, removed all columns but data entry and POS tag

_

- **`processing_scripts`**  contains all processing scripts to be carried out on the files
    - `preprocess_strip_unused_columns` remove all columns but lemma entry and POS tag from a csv conversion of an orginial DIorisis file
    - `process_concatenate_txt_files` concatenates txt files in a folder in a single file. Used to produce training data for fine tuning
    - `process_convert_to_txt` given a dataframe, finda the lemma entries and turns the dataframe into a txt file
    - `process_mask_randomly` given a file, randomly replace any word in a sentence with [MASK] token
    - `process_mask_using_POS_column` given a dataframe from the Diorisis file preprocessing, educately mask words based on POS


### `project_tasks`

- **`ag_fine_tuning`** 

    - `ancient-greek-fine-tuning` script to fine tune AG model on Diorisis corpus on fill-mask downstream task

_

- **`clustering`** contains files and product of the clustering task 
    - `eval_data` csv files with output for the clstering measures of all permutations of all models
    - `graphs` plots saved as png files for all the permutations of all the models
    - `test_model_embeddings_clustering` script to calculate clusters on the text gerne pairs

_

- **`masking`**  contains files and product of the masking task 
    - `eval_data` contains csv evaluation files for both distribution test cases for all models
    - `create_eval_file` script to collate the first 30 lines of the sampled files to create the test data for this task
    - `test_masking` script to calculate tokens given a test file and a model
    - `test_results_cosine_is_1` script to calculate how many tokens have an acceptable cosine similarity score for every model


#

## Getting started

A `requiremetns.txt` file was included in the main folder. The dependencies included in the file are to be installed before code can be run. 

It is also worth noting that multiple file extensions are present:
- `.py` 
- `.ipynb` 

This was chosen for simple convenience of the author. Where code was complex and deemed to run for long periods of time `ipynb` was preferred. This provides flexibility when using previous cached output without the necessity to re-run the more complex apects of the script. 

A _virtual environment_ will be required to run some of the components, especially the `ipynb` files. The code was develped using:
- `anaconda3`

#

## How to use

Individual scripts can be run separately to reproduce results and can be edited to produce new results. 

Due to the constnatly evolving nature of the project and the development necessity of the author of the papaer, always make sure that:

> **source** data folder path alling 

> **destination** data folder are not already populated by other data that will be overwritten

#

## Issues and limitations

The source code is composite of various small testing scripts and there is no general single file to be run to view results. This is proper of the intrinsecally fragmented nature of a research project.
