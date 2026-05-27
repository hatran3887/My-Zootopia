import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def main():
    """Main function"""
    animals_data = load_data('animals_data.json')
    animals_data_string = ''
    for animal in animals_data:
        animals_data_string += '<li class="cards__item">\n'
        animals_data_string += f'Name: {animal["name"]}<br/>\n'
        animals_data_string += f'Diet: {animal["characteristics"]["diet"]}<br/>\n'
        animals_data_string += f'Location: {animal["locations"][0]}<br/>\n'

        animal_type = animal["characteristics"].get("type")
        if animal_type:
            animals_data_string += f'Type: {animal_type}<br/>\n'
        animals_data_string += '</li>\n'

    with open('animals_template.html', 'r') as handle:
        template = handle.read()

    filled_template = template.replace('__REPLACE_ANIMALS_INFO__', animals_data_string)
    with open('animals.html', 'w') as handle:
        handle.write(filled_template)

if __name__ == '__main__':
    main()