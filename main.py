# this is a comment
def encoder(num):
    string = " "
    for i in range(len(num)):
        string += str((int(num[i]) + 3) % 10)
    return string


def main():
    encoded_password = None
    choices = True
    while choices:
        choices = int(input("Menu\n"
                            "-------------\n"
                            "1. Encode\n"
                            "2. Decode\n"
                            "3. Quit \n"
                            "Please enter an option: "))
        if choices == 1:
            num = input("Please enter your password to encode: ")
            encoded_password = encoder(num)
            print("Your password has been encoded and stored! ")
        if choices == 2:
            print(
                f"The encoded password is {encoded_password}, and the original password is .")
            pass
        if choices == 3:
            break


if __name__ == "__main__":
    main()

