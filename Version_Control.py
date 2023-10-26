# Joshua Austin M Land
alpha = True
def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    # menu function
def encode():
    if omega == '1':
        zeta = input('Please enter your password to encode: ')
        theta = ''
        for char in zeta:
            if char.isdigit():
                theta += str(int(char) + 3)
            else:
                theta += char
        print('Your password has been encoded and stored!')
    return theta


while alpha:
    menu()
    omega = input('Please enter an option: ')
    if omega == '1':
        theta = encode()
    elif omega == '3':
        break