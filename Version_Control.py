alpha = True

def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')

    # menu function

    # Joshua Austin M Land
def encode(zeta):

        theta = ''
        for char in zeta:
            if char.isdigit():
                theta += str(int(char) + 3)
            else:
                theta += char

        print('Your password has been encoded and stored!')
        return theta

# Manas Borkar
def decode(theta):

    delta = ''
    for char in theta:
        if char.isdigit():
            delta += str(int(char) - 3)
        else:
            delta += char
    print(f"The encoded password is {theta}, and the original is {delta}")
    return delta


def main():
    while alpha:
        menu()
        omega = input("Please enter an option:")
        if omega == '1':
            zeta = input('Please enter your password to encode: ')
            theta = encode(zeta)
        if omega == '2':
            decode(theta)
        if omega == '3':
            break

if __name__ == '__main__':
    main()
