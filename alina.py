def main():
    create_file("/home/ant/Programming/alina/templates/test.txt.al", girlType="Fat Girls")

def create_file(template_path, **kwargs):
    text = ""
    with open(template_path, 'r') as file:
        text = file.read(-1)

    for key, val in kwargs.items():
        text = text.replace(f'{{{{ {key} }}}}', val)

    print(text)

if __name__ == '__main__':
    main()
