import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_animals():
    animals_data = load_data('animals_data.json')

    output = ""
    for animal in animals_data:
        output += f"Name: {animal['name']}\n"
        output += f"Diet: {animal['characteristics']['diet']}\n"
        output += f"Location: {animal['locations'][0]}\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}\n"

    return output


def generate_html():
    with open('animals_template.html', 'r') as file:
        template = file.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", print_animals())

    with open('animals.html', 'w') as file:
        file.write(template)

generate_html()
