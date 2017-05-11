from unzip_cc_data import import_zip, cc_files
from csv_to_json_config import *
import pandas as pd
import os
import json


def format_table(df, file, columns):
    # Uses the column reformating dictionary in the donfig script to set the column formats
    # The datetimes are written in iso format as specifid in the write_table_to_json function
    if file in column_reformatting:
        for col in columns:
            if col in column_reformatting[file]:
                if column_reformatting[file][col]:
                    if column_reformatting[file][col] == 'datetime':
                        df[col] = pd.to_datetime(df[col], format='%Y-%m-%d %H:%M:%S')
                    else:
                        df[col] = df[col].astype(column_reformatting[file][col], errors='ignore')
    return df


def merge_with_lookup(df, file, all_data_tables):
    # Merges any lookup tables with teh corespoinding data table usung the lookup_table_contexts mapping dictionary in
    # the config file
    if file in lookup_table_contexts:
        for lookup_table in lookup_table_contexts[file]:
            df = df.merge(all_data_tables[lookup_table['csv_name']],
                          how='left',
                          left_on=lookup_table['parent_lookup_cols'],
                          right_on=lookup_table['lookup_cols'])
    return df


def read_all_csvs_to_pd(file_list):
    # Reads all the csvs into memory before performing the necessary table data reformatting and merges
    all_data_tables = {}
    for file in file_list:
        file_name = file + ".csv"
        print('Reading file: ' + file_name)
        all_data_tables[file] = pd.read_csv(file_name, skiprows=[1], error_bad_lines=False, encoding='utf-8',
                                            escapechar="\\", dtype=str)
        all_data_tables[file] = format_table(all_data_tables[file], file, file_list[file])
    for file in file_list:
        all_data_tables[file] = merge_with_lookup(all_data_tables[file], file, all_data_tables)
    return all_data_tables


def add_object(json_target, addition, remaining_address_list, addition_heading, many,
               all_addition_ids):
    # This is the recursive function
    # json_target is a list containing a dictionarys of the charity info
    # the addition is always a list of dictionaries, if many - it should be added as a list, else as extra factors in the parent
    # The specific location that the addition is placed within the target json is dictated by the data_table_contexts in
    # the config script
    address = remaining_address_list[0]
    for item in json_target:
        if item[address['target_id']] == addition[address['addition_id']]:
            if len(remaining_address_list) == 1:
                for id in all_addition_ids:
                    addition.pop(id, None)
                if not many:
                    item.update(addition)
                else:
                    try:
                        item[addition_heading].append(addition)
                    except KeyError:
                        item[addition_heading] = [addition]
                return json_target
            else:
                item[remaining_address_list[1:][0]['parent_object']] = add_object(
                    item[remaining_address_list[1:][0]['parent_object']],
                    addition, remaining_address_list[1:],
                    addition_heading, many, all_addition_ids)
                return json_target


def write_table_to_json(id, table_context, all_data_tables, root_id):
    # Converts a pandas table into a json object inwhich each record with the id specified forms a seperate object with
    # an array of objects, each of which has an attribute for each column in the table
    table_data = all_data_tables[table_context['csv_name']].loc[
        all_data_tables[table_context['csv_name']][root_id] == id]
    table_json = table_data.to_json(orient="records", date_format='iso')
    return json.loads(table_json)


def write_charity_to_json(id, all_data_tables, root_id):
    # Generates a full json object for a given charity based on it's id
    print("Converting charity: " + id)
    charity_json = ""
    for table_context in data_table_contexts:
        if table_context['include']:
            table_json = write_table_to_json(id, table_context, all_data_tables, root_id)
            if not table_context['json_address']:
                charity_json = table_json
            else:
                all_addition_ids = [d['addition_id'] for d in table_context['json_address']]
                for new_object in table_json:
                    charity_json = add_object(charity_json, new_object, table_context['json_address'],
                                              table_context['json_heading'], table_context['many'], all_addition_ids)
    return charity_json


def convert_all_data_to_json(root_dir_name=os.path.dirname(os.path.abspath(__file__)),
                             zip_file="RegPlusExtract_March_2017.zip", id_list=(),
                             csv_folder='charity-commission-extract', extract_data=False,
                             root_id="regno", main_table_name='extract_main_charity',
                             default_charity_count_limit=100):
    # Primary function of script - set extract_data to True to perform the data extract from the original zipped bcp files
    # zip_file should be stored in the csv folder
    os.chdir(os.path.join(root_dir_name, csv_folder))
    if extract_data:
        import_zip(zip_file)

    all_data_tables = read_all_csvs_to_pd(cc_files)
    if not id_list:
        full_id_list = [id for id in list(all_data_tables[main_table_name][root_id])]
        if len(full_id_list) > default_charity_count_limit:
            id_list = full_id_list[:default_charity_count_limit]
        else:
            id_list = full_id_list
    all_charity_json = []
    for id in id_list:
        all_charity_json += write_charity_to_json(id, all_data_tables, root_id)
    os.chdir(os.path.join(root_dir_name))
    return all_charity_json


if __name__ == "__main__":
    example_ouput_name = 'example.json'
    example_json = convert_all_data_to_json(zip_file="RegPlusExtract_January_2017.zip", extract_data=True)
    with open(example_ouput_name, 'w') as feedsjson:
        json.dump(example_json, feedsjson, indent=4, ensure_ascii=True)
