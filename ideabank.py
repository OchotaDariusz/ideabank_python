import sys


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
    try:
        ideas = open_ideas("ideas.txt")
    except IndexError:
        ideas = list()
    finally:
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
