def simple_for_loop(data):
    new_data = []
    for item in data['features']:
        street_name = item['properties'].get('STREET')
        if street_name:
            new_data.append(street_name.lower())
    result = {"new_data": new_data}
    return result


def for_loop_no_dots(data):
    new_data = []
    low = str.lower
    for item in data['features']:
        street_name = item['properties'].get('STREET')
        if street_name:
            new_data.append(low(street_name))
    result = {"new_data": new_data}
    return result


def list_comprehension(data):
    new_data = [item['properties'].get('STREET').lower() for item in data['features']
                if item['properties'].get('STREET') is not None]
    result = {"new_data": new_data}
    return result


def list_comprehension_no_dots(data):
    low = str.lower
    new_data = [low(item['properties'].get('STREET')) for item in data['features']
                if item['properties'].get('STREET') is not None]
    result = {"new_data": new_data}
    return result


def generator_expression(data):
    new_data = (item['properties'].get('STREET').lower() for item in data['features']
                if item['properties'].get('STREET') is not None)
    result = {"new_data": list(new_data)}
    return result

