import json


def load_data():
    """Load data as a dictionary"""
    with open('city.json') as f:
        data = json.load(f)
    return data


def total_slow(data):
    new_data = []
    for item in data['features']:
        street_name = item['properties'].get('STREET')
        if not street_name:
            street_name = 'EMPTY'
        string = ''
        string = string + street_name.lower() + ' '
        from_st, to_st = item['properties']['FROM_ST'], item['properties']['TO_ST']
        string = string + ("%s-%s" % (from_st, to_st)) + ' '
        string = string + item['properties']['BLOCK_NUM']
        string = string + item['properties']['LOT_NUM']
        new_data.append(string)
    result = {"new_data": new_data}
    return result


def total_fast(data):
    low = str.lower
    new_data = [[low(item['properties'].get('STREET'))
                 if item['properties'].get('STREET') else low('EMPTY'),
                 f"{item['properties']['FROM_ST']}-{item['properties']['TO_ST']}",
                 ''.join([item['properties']['BLOCK_NUM'], item['properties']['LOT_NUM']])]
                for item in data['features']]
    result = {"new_data": new_data}
    return result
