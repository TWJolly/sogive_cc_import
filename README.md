# charity-commission-extract
Cloned from https://github.com/ncvo/charity-commission-extract which contains:
Python utilities for handling the import of data from the Charity Commission data.

The additional code handles the conversion of this data from csvs into json and then the adding of that data to an elasticsearch database.

## Get the data

The data can be accessed from <http://data.charitycommission.gov.uk/default.aspx>

Data definition : http://data.charitycommission.gov.uk/data-definition.aspx - these headings are used for the names of the json objects

## Beginner's Guide

A [beginner's guide](beginners-guide.md) to using the Charity Commission data extract.

Marc Lawson at NCVO has also written [a guide to getting the data into a database](https://data.ncvo.org.uk/a/almanac16/how-to-create-a-database-for-charity-commission-data/).

## Using the code in this repo

After downloading the zipped charity commission data, place it in a directory within the project directory. The bcp_to_json.convert_all_data_to_json function can be called with the location of the file as the 'csv_folder' argument, and the name of the zip file as the 'zip_file' argument. 'extract_data' will need to be set to True, otherwise the full set of extracted csvs are expected to exist already. 

convert_all_data_to_json is also called by the elasticsearch_import script which places the data into an ES database.

There are a number of options in convert_all_data_to_json for selecting which ids to use. Note - converting all the data will probably take a very long time.
