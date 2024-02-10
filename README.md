# Password Manager

This Python script serves as a simple password manager that allows users to securely store and view passwords for various accounts. It utilizes the Fernet symmetric encryption scheme from the `cryptography` library to encrypt and decrypt passwords before storing and viewing them, respectively.

## Features

- **Add Password**: Users can add new passwords for different accounts.
- **View Passwords**: Users can view existing passwords for accounts stored in the manager.
- **Secure Encryption**: Passwords are encrypted using Fernet encryption, providing a high level of security.

## Setup

1. Ensure you have Python installed on your system.
2. Install the required dependencies using pip:
   **pip install crypthography**
3. Run the script `password_manager.py`.

## Usage

1. Upon running the script, you will be prompted with options to either add a new password or view existing ones.
2. To add a new password, select the `add` option and provide the account name and password when prompted.
3. To view existing passwords, select the `view` option. The stored account names and their corresponding decrypted passwords will be displayed.
4. You can exit the password manager by typing `q` or `quit` when prompted for an action.

## File Structure

- `password_manager.py`: The main Python script containing the password manager functionality.
- `key.key`: The file where the encryption key is stored. It is generated and loaded automatically by the script.

## Security Considerations

- **Keep Key Secure**: Ensure the `key.key` file containing the encryption key is kept secure and not shared with unauthorized users. Losing this key will result in the inability to decrypt stored passwords.
- **Secure Passwords**: Although passwords are encrypted, it's essential to use strong, unique passwords for each account to enhance security further.

## Disclaimer

This password manager is intended for educational purposes and may not provide the same level of security as commercial password management solutions. Use it at your own risk and ensure proper precautions are taken to safeguard your passwords and encryption key.

