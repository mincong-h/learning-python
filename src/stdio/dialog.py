def main():
    should_continue = show_dialog("Welcome to Mincong's demo")
    if should_continue:
        print("Thanks for confirmation")
    else:
        print("Sorry to see you go")


def show_dialog(text: str) -> bool:
    print(text)
    while True:
        answer = input("Do you want to continue[Y/n]?")
        if answer.lower() in ["y", "n"]:
            return answer.lower() == "y"


if __name__ == "__main__":
    main()
