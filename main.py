# this is a comment from Xinchen Yao
def encoder(num):
    string = ""
    for i in range(len(num)):
        string += str((int(num[i]) + 3) % 10)
    return string


def decoder(encoded_password):
    password = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)  # shift down by 3
        password += original_digit
    return password


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

            password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")

        if choices == 3:
            break


if __name__ == "__main__":
    main()

