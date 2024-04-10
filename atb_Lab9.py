#Aiden Bentz

def encode(password):
    encoded_pass = ""
    for i in range(0, len(password)):
        x = int(password[i]) + 3
        if x > 9:
            x -= 10
        encoded_pass += str(x)
    return encoded_pass


def decode(en):
    decoded_pass = ""
    for i in range(0, len(en)):
        temp = int(en[i])
        temp -= 3
        if temp < 0:
            temp += 10
        decoded_pass += str(temp)
    return decoded_pass


if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.\n")
        elif option == 3:
            break
