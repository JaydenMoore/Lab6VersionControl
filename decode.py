# Nicholas Lucky made the decode() function for this program!

# Takes in an encoded password, and shifts each digit back by 3 before returning the decrypted password back!
def decode(encoded_password):
    decoded_password = ""  # Stores the decrypted password that will be added to and returned back

    for digit in encoded_password:  # For each digit in the encoded password...
        decoded_password += str(int(digit) - 3)  # Shift the digit back by 3, and add it to decoded_password

    return decoded_password  # Return the decrypted password back!
