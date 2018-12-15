def concat_plus(data):
    new_data = []
    for item in data['features']:
        string = ''
        string = string + item['properties']['BLOCK_NUM']
        string = string + item['properties']['LOT_NUM']
        new_data.append(string)
    result = {"new_data": new_data}
    return result


def concat_plus_is(data):
    new_data = []
    for item in data['features']:
        string = ''
        string += item['properties']['BLOCK_NUM']
        string += item['properties']['LOT_NUM']
        new_data.append(string)
    result = {"new_data": new_data}
    return result


def concat_join(data):
    new_data = []
    for item in data['features']:
        string = ''.join([item['properties']['BLOCK_NUM'], item['properties']['LOT_NUM']])
        new_data.append(string)
    result = {"new_data": new_data}
    return result
