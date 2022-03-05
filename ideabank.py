import argparse


parser = argparse.ArgumentParser()

parser.add_argument('-l', '--list', help='Lists all ideas', action='store_true', required=False)

parser.add_argument('-d',
                    '--delete',
                    type=int,
                    help='Specify a number of idea to delete',
                    required=False)


args = parser.parse_args()


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
        if not args.list and not args.delete:
            while True:
                if ideas:
                    for index in range(len(ideas)):
                        print(f"{index + 1}. {ideas[index]}")
                idea = input("What is your new idea?\n")
                ideas.append(idea)
                export_ideas("ideas.txt", ideas)

        if args.list:
            if ideas:
                for index in range(len(ideas)):
                    print(f"{index + 1}. {ideas[index]}")
            else:
                print("There's no ideas!")

        if args.delete:
            if ideas:
                try:
                    ideas.pop(int(args.delete) - 1)
                    export_ideas("ideas.txt", ideas)
                except IndexError:
                    print("There's no so many ideas!")
            else:
                print("There's no ideas!")
