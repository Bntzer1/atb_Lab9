#Aiden Bentz

def encode(password):
    encoded_pass = ""
    for i in range(0, len(password)):
        x = int(password[i]) + 3
        if x > 9:
            x -= 10
        encoded_pass += str(x)
    return encoded_pass

if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 3:
            break