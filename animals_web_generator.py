import json


def load_data(file_path):
    """ Load data from file and return it """
    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return []


def generate_animal(animal):
    """Generate HTML for each animal"""
    # Titel of animals
    card_title = f'<div class="card__title">{animal.get("name", "Unbekannt").upper()}</div>'

    # Start HTML text
    card_text = "<p class='card__text'>"

    # Diet-Information
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Not given")
    card_text += f"<strong>Diet:</strong> {diet}<br/>"

    # Location-Informationen
    locations = animal.get("locations", [])
    location = locations[0] if locations else "Not given"
    card_text += f"<strong>Location:</strong> {location}<br/>"

    # Animal Typ
    animal_type = characteristics.get("type", "Not given")
    card_text += f"<strong>Type:</strong> {animal_type}<br/>"

    # End HTML text
    card_text += "</p>"

    # Create complete card in HTML
    full_card = f'<li class="cards__item">\n{card_title}\n{card_text}\n</li>'

    return full_card


def generate_animal_info(file_path):
    """Load data from file and create HTML for each animal """
    animals = load_data(file_path)
    #List for HTML-Elements
    output_list = []

    for animal in animals:
        animal_card = generate_animal(animal)
        output_list.append(animal_card)

    full_html = "<ul class='cards'>\n" + "\n".join(output_list) + "\n</ul>"
    #Returns a list with HTML items
    return full_html


def load_template(template_datei):
    """read HTML File and return it"""
    with open(template_datei, "r", encoding="utf-8") as file:
        return file.read()


def replace_placeholder(template, animal_html):
    """Replace placeholder with animal_html data"""
    return template.replace("__REPLACE_ANIMALS_INFO__", animal_html)


def save_html(filename, content):
    """ Store HTML file """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except IOError:
        print(f"Fehler: Datei {filename} konnte nicht gespeichert werden.")


def main():
    # Generate HTML for each animal
    animal_html = generate_animal_info("animals_data.json")

    # Load HTML Template
    html_content = load_template("animals_template.html")

    # Replace placeholder with animal_html data.
    html_content = replace_placeholder(html_content, animal_html)

    # Store final HTML file
    save_html("animals.html", html_content)


if __name__ == "__main__":
    main()
