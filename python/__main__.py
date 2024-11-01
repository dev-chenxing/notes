import mistune
import random
import os


markdown = mistune.create_markdown(renderer=None)

topics = []


def main():
    path = "math/linear-algebra"
    for entry in os.scandir(path):
        if entry.is_file():
            with open(os.path.join(path, entry.name), encoding="utf-8") as f:
                md = markdown(f.read())
                for token in md:
                    if token['type'] == 'paragraph':
                        t = token['children'][0]
                        if t['type'] == 'strong':
                            topics.append(t['children'][0]['raw'])
    print(random.choice(topics))


if __name__ == '__main__':
    main()
