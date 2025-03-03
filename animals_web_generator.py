import json

def load_data(file_path):
    """ loads data from a json file. """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals_info(file_path):
    """ Returns a list with animals information for all animals"""
    animals = load_data(file_path)
    output_list = []

    for animal in animals:
        output = [] # create a list to store the output for one animal

        if "name" in animal:
            output.append(f"Name: {animal['name']}<br/>")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output.append(f"Diet: {animal['characteristics']['diet']}<br/>")
        if "locations" in animal and len(animal["locations"]) > 0:
            output.append(f"Location: {animal['locations'][0]}<br/>")
        if "type" in animal:
            output.append(f"Type: {animal['type']}<br/>")

        if output:  # only append if there is any data
            output_list.append(f'<li class="cards__item">\n{"".join(output)}\n</li>')

    return output_list # returns a list with html-formatted strings
