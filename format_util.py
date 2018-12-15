def format_percentage(data):
    new_data = []
    for item in data['features']:
        from_st, to_st = item['properties']['FROM_ST'], item['properties']['TO_ST']
        new_data.append("%s-%s" % (from_st, to_st))
    result = {"new_data": new_data}
    return result

def format_dot_format(data):
    new_data = []
    for item in data['features']:
        from_st, to_st = item['properties']['FROM_ST'], item['properties']['TO_ST']
        new_data.append("{}-{}".format(from_st, to_st))
    result = {"new_data": new_data}
    return result


def format_f_string(data):
    new_data = []
    for item in data['features']:
        from_st, to_st = item['properties']['FROM_ST'], item['properties']['TO_ST']
        new_data.append(f"{from_st}, {to_st}")
    result = {"new_data": new_data}
    return result
