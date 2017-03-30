from unzip_cc_data import import_zip, cc_files
import pandas as pd

#Change this to the location of downloaded data
path_to_cc_zip = "RegPlusExtract_March_2017.zip"


basic_charity_info = 'extract_charity'
classification_refernece = 'extract_class_ref'

#import_zip(path_to_cc_zip)
all_data_tables = {}

for file in cc_files:
    file_name = file + ".csv"
    print('Reading file: '+file_name)
    all_data_tables[file] = pd.read_csv(file_name, skiprows=[1], error_bad_lines = False, encoding='utf-8')

