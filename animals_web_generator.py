import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, 'r') as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')
    animals_data_string = ''
    for animal in animals_data:
        animals_data_string += f'Name: {animal["name"]}\n'
        animals_data_string += f'Diet: {animal["characteristics"]["diet"]}\n'
        animals_data_string += f'Location: {animal["locations"][0]}\n'

        animal_type = animal["characteristics"].get("type")
        if animal_type:
            animals_data_string += f'Type: {animal_type}\n'
        animals_data_string += '\n'

    with open('animals_template.html', 'r') as handle:
        template = handle.read()

    filled_template = template.replace('__REPLACE_ANIMALS_INFO__', animals_data_string)

    with open('animals.html', 'w') as handle:
        handle.write(filled_template)

if __name__ == '__main__':
    main()