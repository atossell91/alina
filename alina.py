#! usr/bin/python/python3

import os
import sys
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

def get_top_level_dir():
    path = os.getcwd()
    max_hops = 100
    hops = 0

    while hops < max_hops:
        contents = os.listdir(path)
        if 'src' in contents and 'include' in contents:
            return path
        parent = os.path.dirname(path)
        if parent == path:
            break  # Reached root
        path = parent
        hops += 1

    return None

if __name__ == '__main__':
    main()
