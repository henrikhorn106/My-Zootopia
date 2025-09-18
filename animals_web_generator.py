import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals():
    animals_data = load_data('animals_data.json')

    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += "</li>"

    return output


def generate_html():
    with open('animals_template.html', 'r') as file:
        template = file.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", print_animals())

    with open('animals.html', 'w') as file:
        file.write(template)

generate_html()
