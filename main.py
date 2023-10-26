#Jayden Moore Lab 6
def main():

    encoded_password = ""

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = int(input("Please enter an option: "))

    if option == 1:
        #Encodes the password and stores it within the main function
        original_password = input("Please enter your password to encode: ")
        encoded_password = encode(original_password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        #Decodes the password and informs the user of the new password
        password = input("Please enter your password to decode: ")
        decoded_password = decode(password)
        print(f"The encoded password is {password}, and the original password is {decoded_password}.")
    else:
        exit()

#Takes a password and adds 3 to each integer in the string.
def encode(password):
    encoded_password = ""
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password


# Nicholas Lucky made the decode() function for this program!

# Takes in an encoded password, and shifts each digit back by 3 before returning the decrypted password back!
def decode(encoded_password):
    decoded_password = ""  # Stores the decrypted password that will be added to and returned back

    for digit in encoded_password:  # For each digit in the encoded password...
        decoded_password += str(int(digit) - 3)  # Shift the digit back by 3, and add it to decoded_password

    return decoded_password  # Return the decrypted password back!

main()