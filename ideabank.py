import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--list', type=int, required=False)
parser.add_argument('--delete', type=int, required=False)


def open_ideas(file_name):
    with open(file_name, "r+") as file:
        lines = file.readlines()
    elements = [element.replace("\n", "").split(";") for element in lines]
    return elements[0]


def export_ideas(file_name, elements):
    with open(file_name, "w") as file:
        ideas = ';'.join(elements)
        file.write(ideas + "\n")


if __name__ == "__main__":
    ideas = open_ideas("ideas.txt")
    print(ideas)
    while True:
        if ideas:
            for index in range(len(ideas)):
                print(f"{index + 1}. {ideas[index]}")
        idea = input("What is your new idea?\n")
        ideas.append(idea)
        export_ideas("ideas.txt", ideas)
