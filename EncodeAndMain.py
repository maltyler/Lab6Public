# Mallory Tyler's original code (without decode method)
# The password encoder should take in an 8-digit password
# in string format containing only integers
# After passing the password into the encoder, the encoder
# stores the encoded password to a new variable, with each
# digit being shifted up by 3 numbers.
def encode(password):
    encoded_password = ""
    for integer in password:
        # 7 changes to 0
        if int(integer) == 7:
            encoded_password += "0"
        # 8 changes to 1
        elif int(integer) == 8:
            encoded_password += "1"
        # 9 changes to 2
        elif int(integer) == 9:
            encoded_password += "2"
        # all others just add 3
        else:
            encoded_password += str(int(integer) + 3)
    return encoded_password

# main function
def main():
    # while loop so that the menu loops
    continue_program = True
    while continue_program:
        # print the menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        # ask the user to choose 1, 2, or 3
        option = int(input("Please enter an option: "))

        # encode option
        if option == 1:
            password = input("Please enter your password to encode: ")

            # encodes the password
            encoded = encode(password)

            print("Your password has been encoded and stored!")
            print()

        # decode option
        elif option == 2:
            print(f'The encoded password is {encoded}, and the original password is {password}.')
            print()

        # quit option
        else:
            continue_program = False

if __name__ == "__main__":
    main()