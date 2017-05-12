# These dictate how reference tables should be added to their parent tables
lookup_table_contexts = {
    "extract_charity_aoo": [{
        "csv_name": "extract_aoo_ref",
        "lookup_cols": ['aootype', 'aookey'],
        "parent_lookup_cols": ['aootype', 'aookey']
    }],
    "extract_class": [{
        "csv_name": "extract_class_ref",
        "lookup_cols": ['classno'],
        "parent_lookup_cols": ['class']
    }],
    "extract_registration": [{
        "csv_name": "extract_remove_ref",
        "lookup_cols": ['code'],
        "parent_lookup_cols": ['remcode']}]
}

# These dictate how a csv should be placed within the wider json structure by the recursive bcp_to_json.add_object function
data_table_contexts = [
    {"csv_name": 'extract_main_charity',
     "include": True,
     "json_address": False
     },
    {"csv_name": 'extract_acct_submit',
     "include": True,
     "json_heading": "acct_submit",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_ar_submit',
     "include": True,
     "json_heading": "ar_submit",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_charity',
     "include": True,
     "json_heading": "subcharities",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_charity_aoo',
     "include": True,
     "json_heading": "aoo",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_class',
     "include": True,
     "json_heading": "classes",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_financial',
     "include": True,
     "json_heading": "financial",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_name',
     "include": True,
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'},
                      {'parent_object': "subcharities", 'target_id': 'subno', 'addition_id': 'subno'}],
     "json_heading": "extract_name",
     "many": True
     },
    {"csv_name": 'extract_objects',
     "include": True,
     "json_heading": "objects",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'},
                      {'parent_object': "subcharities", 'target_id': 'subno', 'addition_id': 'subno'}],
     "many": True
     },
    {"csv_name": 'extract_partb',
     "include": True,
     "json_heading": "accountspartb",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     },
    {"csv_name": 'extract_registration',
     "include": True,
     "json_heading": False,
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'},
                      {'parent_object': "subcharities", 'target_id': 'subno', 'addition_id': 'subno'}],
     "many": False
     },
    {"csv_name": 'extract_trustee',
     "include": True,
     "json_heading": "trustee_list",
     "json_address": [{'target_id': 'regno', 'addition_id': 'regno'}],
     "many": True
     }
]

# These assign column formats for each column in  each table, blank formats are left unchanged - by default all data is
# read in as strings
column_reformatting = {
    "extract_acct_submit": {
        "regno": "",
        "submit_date": 'datetime',
        "arno": "",
        "fyend": ""
    },
    "extract_aoo_ref": {
        "aootype": "",
        "aookey": "",
        "aooname": "",
        "aoosort": "",
        "welsh": "",
        "master": ""
    },
    "extract_ar_submit": {
        "regno": "",
        "arno": "",
        "submit_date": "datetime"
    },
    "extract_charity": {
        "regno": "",
        "subno": "",
        "name": "",
        "orgtype": "",
        "gd": "",
        "aob": "",
        "aob_defined": "",
        "nhs": "",
        "ha_no": "",
        "corr": "",
        "add1": "",
        "add2": "",
        "add3": "",
        "add4": "",
        "add5": "",
        "postcode": "",
        "phone": "",
        "fax": "",
    },
    "extract_charity_aoo": {
        "regno": "",
        "aootype": "",
        "aookey": "",
        "welsh": "",
        "master": ""
    },
    "extract_class": {
        "regno": "str",
        "class": ""
    },
    "extract_class_ref": {
        "classno": "",
        "classtext": "",
    },
    "extract_financial": {
        "regno": "",
        "fystart": "datetime",
        "fyend": "datetime",
        "income": "float",
        "expend": "float"
    },
    "extract_main_charity": {
        "regno": "",
        "coyno": "",
        "trustees": "",
        "fyend": "",
        "welsh": "",
        "incomedate": "datetime",
        "income": "float",
        "grouptype": "",
        "email": "",
        "web": ""
    },
    "extract_name": {
        "regno": "",
        "subno": "",
        "nameno": "",
        "name": ""
    },
    "extract_objects": {
        "regno": "",
        "subno": "",
        "seqno": "",
        "object": ""
    },
    "extract_partb": {
        "regno": "",
        "artype": "",
        "fystart": "datetime",
        "fyend": "datetime",
        "inc_leg": "float",
        "inc_end": "float",
        "inc_vol": "float",
        "inc_fr": "float",
        "inc_char": "float",
        "inc_invest": "float",
        "inc_other": "float",
        "inc_total": "float",
        "invest_gain": "float",
        "asset_gain": "float",
        "pension_gain": "float",
        "exp_vol": "float",
        "exp_trade": "float",
        "exp_invest": "float",
        "exp_grant": "float",
        "exp_charble": "float",
        "exp_gov": "float",
        "exp_other": "float",
        "exp_total": "float",
        "exp_support": "float",
        "exp_dep": "float",
        "reserves": "float",
        "asset_open": "float",
        "asset_close": "float",
        "fixed_assets": "float",
        "open_assets": "float",
        "invest_assets": "float",
        "cash_assets": "float",
        "current_assets": "float",
        "credit_1": "float",
        "credit_long": "float",
        "pension_assets": "float",
        "total_assets": "float",
        "funds_end": "float",
        "funds_restrict": "float",
        "funds_unrestrict": "float",
        "funds_total": "float",
        "employees": "float",
        "volunteers": "float",
        "cons_acc": "",
        "charity_acc": ""
    },
    "extract_registration": {
        "regno": "",
        "subno": "",
        "regdate": "datetime",
        "remdate": "datetime",
        "remcode": ""
    },
    "extract_remove_ref": {
        "code": "",
        "text": ""
    },
    "extract_trustee": {
        "regno": "",
        "trustee": ""
    }
}
