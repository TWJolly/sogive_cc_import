from unzip_cc_data import import_zip, cc_files
import pandas as pd
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
csv_file_dir = 'test_csvs'
os.chdir(os.path.join(dir_name, csv_file_dir))

path_to_cc_zip = "RegPlusExtract_March_2017.zip" #Change this to the location of downloaded data
#import_zip(path_to_cc_zip) #Uncomment to perform the extract from bcp files

all_data_tables = {}
for file in cc_files:
    file_name = file + ".csv"
    print('Reading file: '+file_name)
    all_data_tables[file] = pd.read_csv(file_name, skiprows=[1], error_bad_lines = False, encoding='utf-8')
    print(all_data_tables)

