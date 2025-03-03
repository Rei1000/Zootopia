import json

def load_data(file_path):
    """ Lädt die JSON-Datei und gibt die Daten zurück. """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def print_animals_info(file_path):
    """ Liest die JSON-Daten und gibt Name, Diet, Location & Type aus """
    animals = load_data(file_path)
    output_list = []

    for animal in animals:
        output = []

        if "name" in animal:
            output.append(f"Name: {animal['name']}")
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output.append(f"Diet: {animal['characteristics']['diet']}")
        if "locations" in animal and len(animal["locations"]) > 0:
            output.append(f"Location: {animal['locations'][0]}")
        if "type" in animal:
            output.append(f"Type: {animal['type']}")

        if output:  # Nur ausgeben, wenn es Daten gibt
            output_list.append(f"<li>{'<br>'.join(output)}</li>")

    return output_list
