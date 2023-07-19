def encode_num(num_str):
    encoded_str = ""
    for num in num_str:
        encoded_str += str((int(num) + 3) % 10)
    return encoded_str


def main():
    i = True
    while i:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode_num(password)
            print("Your password has been encoded and stored!\n")
        # implement decode function here
        elif menu_choice == 3:
            break


if __name__ == "__main__":
    main()


