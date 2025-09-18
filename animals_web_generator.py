"""
This module provides functionality to load data from a file, format specific
data into HTML, and generate an HTML file based on template replacement.

Functions:
- load_data: Loads JSON data from a specified file.
- create_animals_html: Fetches and formats animal data into HTML list item strings.
- generate_html: Generates an HTML file by replacing placeholders in a
  template with formatted animal data.
"""
import json


def load_data(file_path):
    """Loads JSON data from a specified file."""

    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes an animal object into a string."""

    output = ''
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj['name']}</div>\n'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    output += "</p>"
    output += "</li>"

    return output


def create_animals_html():
    """Fetches and formats animal data into HTML list item strings."""

    animals_data = load_data('animals_data.json')

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def generate_html():
    """Generates an HTML file by replacing placeholders in a template with formatted animal data."""

    with open('animals_template.html', 'r', encoding="utf-8") as file:
        template = file.read()

    template = template.replace("__REPLACE_ANIMALS_INFO__", create_animals_html())

    with open('animals.html', 'w', encoding="utf-8") as file:
        file.write(template)


if __name__ == "__main__":
    generate_html()
