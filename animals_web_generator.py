"""
Animals Web Generator
"""
import json

REPLACE_TEMPLATE_TEXT = '__REPLACE_ANIMALS_INFO__'


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes an animal object"""
    animal_string = ''
    animal_string += '<li class="cards__item">\n'
    animal_string += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    animal_string += '<p class="card__text">\n'
    animal_string += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    animal_string += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    animal_type = animal_obj["characteristics"].get("type")
    if animal_type:
        animal_string += f'<strong>Type:</strong> {animal_type}<br/>\n'
    animal_string += '</p>\n'
    animal_string += '</li>\n'
    return animal_string


def main():
    """Main function"""
    animals_data = load_data('animals_data.json')
    animals_data_string = ''
    for animal in animals_data:
        animals_data_string += serialize_animal(animal)

    with open('animals_template.html', 'r') as handle:
        template = handle.read()

    filled_template = template.replace(REPLACE_TEMPLATE_TEXT, animals_data_string)
    with open('animals.html', 'w') as handle:
        handle.write(filled_template)

if __name__ == '__main__':
    main()