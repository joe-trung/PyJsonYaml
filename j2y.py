import json
import yaml


def j2y_converter(input_file, output_file):
    with open(input_file) as f:
        data = json.load(f)

    yaml_string = yaml.dump(data)

    with open(output_file, "w") as f:
        f.write(yaml_string)


j2y_converter('/Users/trung/Python Projects/PyJsonYaml/donuts.json', '/Users/trung/Python Projects/PyJsonYaml/donuts.yaml')
j2y_converter('/Users/trung/Python Projects/PyJsonYaml/emojis.json', '/Users/trung/Python Projects/PyJsonYaml/emojis.yaml')


def y2j_converter(input_file, output_file):
    with open(input_file) as f:
        data = yaml.safe_load(f)

    json_string = json.dumps(data)

    with open(output_file, "w") as f:
        f.write(json_string)

y2j_converter('/Users/trung/Python Projects/PyJsonYaml/verify.yaml', '/Users/trung/Python Projects/PyJsonYaml/verify.json')
y2j_converter('/Users/trung/Python Projects/PyJsonYaml/xmas.yaml', '/Users/trung/Python Projects/PyJsonYaml/xmas.json')