import scrypt

def encrypt(filename, password):
    '''
    Given a filename (str) and password (str), encrypts the file and overwrites it
    '''
    with open(filename, 'rb') as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = scrypt.encrypt(file_data, password)
    # write the encrypted file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decrypt(filename, password):
    '''
    Given a filename (str) and password (str), decrypts the file and overwrites
    '''
    with open(filename, 'rb') as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = scrypt.decrypt(encrypted_data, password)

    # write the original file
    with open(filename, 'w') as file:
        file.write(decrypted_data)
    print('File decrypted successfully')
