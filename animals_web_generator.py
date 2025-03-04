import json

def load_data(file_path):
    """ loads data from a json file and returns it. """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def serialize_animal(animal):
    """create HTML for each animal """
    #Animal title
    card_title = f'<div class="card__title">{animal["name"].upper()}</div>'

    # Start HTML-Text
    card_text = "<p class='card__text'>"

    #Diet Information
    if "characteristics" in animal:
        if "diet" in animal["characteristics"]:
            diet = animal["characteristics"]["diet"]
            card_text += f"<strong>Diet:</strong> {diet}<br/>"

    # Locations Information
    if "locations" in animal and len(animal["locations"]) > 0:
        location = animal["locations"][0]
        card_text += f"<strong>Location:</strong> {location}<br/>"

    # Characteristics Information
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animal_type = animal["characteristics"]["type"]
        card_text += f"<strong>Type:</strong> {animal_type}<br/>"

        # End HTML-Text
    card_text += "</p>"

    # Create full card in HTML
    full_card = f'<li class="cards__item">\n{card_title}\n{card_text}\n</li>'

    return full_card

def print_animals_info(file_path):
    """ Load data from file and create HTML for each animal """
    animals = load_data(file_path)
    #List for HTML-Elements
    output_list = []

    for animal in animals:
        animal_card = serialize_animal(animal)
        output_list.append(animal_card)

    full_html = "<ul class='cards'>\n" + "\n".join(output_list) + "\n</ul>"
    #returns  list with HTML items
    return full_html

