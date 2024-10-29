import mistune
import random


markdown = mistune.create_markdown(renderer=None)

topics = []


def main():
    with open("linear-algebra/chapter-3-vectors-向量组.md", encoding="utf-8") as f:
        md = markdown(f.read())
        for token in md:
            if token['type'] == 'paragraph':
                for child in token['children']:
                    if child['type'] == 'strong':
                        topics.append(child['children'][0]['raw'])
    print(random.choice(topics))


if __name__ == '__main__':
    main()
