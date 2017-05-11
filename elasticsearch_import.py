import elasticsearch as es
from bcp_to_json import *
import requests

# This script adds a json object to the specified elastic search instance.
# Each charity is added with an is that is it's root_id

root_id = 'regno'
index_name = 'charity_commision_data'
document_type = 'charity'
es_host = "localhost"
es_port = 9200
es_address = 'http://localhost:9200'

id_list = []

connection = es.Elasticsearch([{'host': es_host, 'port': es_port}])
res = requests.get(es_address)

all_charity_json = convert_all_data_to_json(id_list=[], root_id=root_id)

for charity in all_charity_json:
    connection.index(index=index_name, doc_type=document_type, id=charity[root_id], body=charity)

# print(connection.get(index=index_name, doc_type=document_type, id='1105319'))
