import argparse

def main():
    args = argparse.ArgumentParser("Alina")
    args.add_argument("command", help="The command to execute", choices=[
        "class", "header", "interface", "namespace"
    ])

    args.add_argument("-name", help="The file name")
    args.add_argument("-namespace", help="The namespace to use")

    args.parse_args()

def create_file(template_path, **kwargs):
    text = ""
    with open(template_path, 'r') as file:
        text = file.read(-1)

    for key, val in kwargs.items():
        text = text.replace(f'{{{{ {key} }}}}', val)

    print(text)

def get_current_folder():
    pass

if __name__ == '__main__':
    main()
