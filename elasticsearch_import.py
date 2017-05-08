import elasticsearch as es
from bcp_to_json import *

# This script adds a json object to the specified elastic search instance.
# Each charity is added with an is that is it's root_id

root_id = 'regno'

import requests

connection = es.Elasticsearch([{'host': 'localhost', 'port': 9200}])
res = requests.get('http://localhost:9200')

id_list = []

all_charity_json = convert_all_data_to_json(id_list=[], root_id=root_id)

for charity in all_charity_json:
    connection.index(index='charity_commision_data', doc_type='charity', id=charity[root_id], body=charity)

print(connection.get(index='charity_commision_data', doc_type='charity', id='1105319'))
