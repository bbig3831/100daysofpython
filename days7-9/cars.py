cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = cars['Jeep']
    return ', '.join(jeeps)


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    models = [model[0] for model in cars.values()]
    return models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    match_list = []
    for value in cars.values():
        matches = [model for model in value if grep.lower() in model.lower()]
        match_list = match_list + matches

    match_list.sort()
    return match_list


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for value in cars.values():
        value.sort()

    return cars