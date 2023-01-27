
class world_sys:
    def __init__(self, input_name):
        self.name = input_name

def main():

    print("PYPY OFFLINE MUD")
    print("TESTING TESTING, ONE-TWO, TESTING")
    print("\n\n(c) 2023 SATELLITE")
    print("(c) 2023 PARADIGM CORPORATION")
    print("(c) WATTSON SOFTWARE PRODUCTS")
    print("--------------------------------------------------")
    print("the line above is 50 charz, okay?")

    local_user_input = "void"

    print("\n\n")
    print("enTer a world name!")
    print("[PYPYOM]>>", end="")
    local_user_input = input()

    print("do you want to use the word, " + str(local_user_input) + ", for your world?")
    print("type yes/no:", end="")
    question_input = input()

    if question_input == "yes" || question_input == "y" || question_input == "yea":
        print("affirmative received!@")

    if question_input == "no" || question_input == "n" || if question_input == "nah":
        while question_input != "yes" || question_input != "y" || question_input != "yea":
            print("type \"random\" for a random world name")
            print("enter a world name...")

            print("PYPYOM>>")
            question_input = input()

            if question_input == "random":
                random_bit = True

            print("is this the name you want to use? (" + str(question_input) + ")")

    print("error end of code")

if __name__ == "__main__":
    main()