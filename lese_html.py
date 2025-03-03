from animals_web_generator import print_animals_info

def load_template(template_datei):
    """ read HTML File and return it """
    with open(template_datei, "r", encoding="utf-8") as file:
        return file.read()


def replace_placeholder(template, animal_html):
    """ Replace placeholder with animal_html data """
    return template.replace("__REPLACE_ANIMALS_INFO__", animal_html)


def save_html(dateiname, content):
    """ Save HTML File """
    with open(dateiname, "w", encoding="utf-8") as file:
        file.write(content)

# call the funktion to get the animal data
output_list = print_animals_info("animals_data.json")

#make a string from the list
animal_html = "\n".join(output_list)

# load HTML-Template
html_content = load_template("animals_template.html")

#replace the placeholder in the template with the animal data
html_content = replace_placeholder(html_content, animal_html)

#save the HTML-File
save_html("animals.html", html_content)

print("animals.html are created")


