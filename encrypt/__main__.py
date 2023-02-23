import getpass
from encrypt.encrypt import encrypt
from encrypt.encrypt import decrypt

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='File Encryptor Script with a Password')
    parser.add_argument('file', help='File to encrypt/decrypt')
    parser.add_argument('-e', '--encrypt', action='store_true',
                        help='Whether to encrypt the file, only -e or -d can be specified.')
    parser.add_argument('-d', '--decrypt', action='store_true',
                        help='Whether to decrypt the file, only -e or -d can be specified.')

    args = parser.parse_args()
    file = args.file

    if args.encrypt:
        password = getpass.getpass('Enter the password for encryption: ')
    elif args.decrypt:
        password = getpass.getpass('Enter the password you used for encryption: ')

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError('Please specify whether you want to encrypt the file or decrypt it.')
    elif encrypt_:
        encrypt(file, password)
    elif decrypt_:
        decrypt(file, password)
    else:
        raise TypeError('Please specify whether you want to encrypt the file or decrypt it.')
    