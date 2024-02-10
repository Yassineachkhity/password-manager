from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    write_key()
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def view(fer):
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
           data = line.rstrip()
           user, passw = data.split("|")
           print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode() )
           

def add(fer):
    name = input("Account Name: ")
    password = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n") 

def main():
    key = load_key()
    fer = Fernet(key)
    
    while True:
        print("Would you like to add a new password or view existing ones")
        mode = input("Type view or add or press q to quit: ").lower()
        
        if mode in ['q', 'quit']:
            break
        
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid mode.")
            continue
if __name__ == "__main__":
    main()