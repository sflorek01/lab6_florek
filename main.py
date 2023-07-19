def encode(num_str):
    encoded_str = ""
    for num in num_str:
        encoded_str += str((int(num) + 3) % 10)
    return encoded_str

def decode_password(encoded_str):  # code implemented by Armando Cruz
    decoded_password = ""
    for number in encoded_str:
        new_digit = str((int(number) - 3) % 10)
        decoded_password += new_digit
    return decoded_password

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
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        # implement decode function here
        if menu_choice == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}\n")
        elif menu_choice == 3:
            break


if __name__ == "__main__":
    main()


