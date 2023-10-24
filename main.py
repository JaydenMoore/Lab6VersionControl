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
    else:
        #Decodes the password and informs the user of the new password
        password = input("Please enter your password to decode: ")

#Takes a password and adds 3 to each integer in the string.
def encode(password):
    encoded_password = ""
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password

def decode():
    pass

main()