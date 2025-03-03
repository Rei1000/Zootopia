import json

def load_data(file_path):
    """ loads data from a json file and returns it. """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals_info(file_path):
    """ Returns a list with formatted HTML cards for all animals"""
    animals = load_data(file_path)

    output_list = []

    for animal in animals:
        # Animal title in upper letters
        if "name" in animal:
            card_title = f'<div class="card__title">{animal["name"].upper()}</div>'
        else:
            card_title = ""

        #Variable for the animal details as HTML
        card_text = "<p class='card__text'>"

        #append animal diet
        if "characteristics" in animal:
            if "diet" in animal["characteristics"]:
               diet = animal["characteristics"]["diet"]
               card_text += f"<strong>Diet:</strong> {diet}<br/>"

        #append animal location
        if "locations" in animal:
            if animal["locations"]: #check if list is not empty
                location = animal["locations"][0]
                card_text += f"<strong>Location:</strong> {location}<br/>"

        #append animal type
        if "characteristics" in animal:
            if "type" in animal["characteristics"]:
                animal_type = animal["characteristics"]["type"]
                card_text += f"<strong>Type:</strong> {animal_type}<br/>"

        card_text += "</p>"

        #complete animal card as list item
        full_card = f'<li class="cards__item">\n{card_title}\n{card_text}\n</li>'
        output_list.append(full_card)

    #returns list with HTML items
    return output_list

