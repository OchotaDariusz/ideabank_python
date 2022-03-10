import sys


def open_ideas(file_name):
    try:
        file = open(file_name, "r+").readlines()
        elements = [element.replace("\n", "").split(";") for element in file]
    except FileNotFoundError:
        file = open(file_name, "w")
        elements = list()
    if elements:
        return elements[0]
    else:
        return elements


def export_ideas(file_name, elements):
    with open(file_name, "w") as file:
        ideas = ';'.join(elements)
        file.write(ideas + "\n")


if __name__ == "__main__":
    ideas = open_ideas("ideas.txt")
    if len(sys.argv) == 1:
        while True:
            if ideas:
                for index in range(len(ideas)):
                    print(f"{index + 1}. {ideas[index]}")
            idea = input("What is your new idea?\n")
            ideas.append(idea)
            export_ideas("ideas.txt", ideas)

    elif sys.argv[1] == "--list":
        if ideas:
            for index in range(len(ideas)):
                print(f"{index + 1}. {ideas[index]}")
        else:
            print("There's no ideas!")

    elif sys.argv[1] == "--delete":
        try:
            if ideas:
                try:
                    ideas.pop(int(sys.argv[2]) - 1)
                    export_ideas("ideas.txt", ideas)
                except IndexError:
                    raise ValueError
            else:
                print("There's no ideas!")
        except ValueError:
            print("Specify a number after --delete")
