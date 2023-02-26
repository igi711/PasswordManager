from colored import fg
from cryptography.fernet import Fernet
from datetime import datetime
import pyfiglet

red = fg('red')
blue = fg('cyan')
green = fg('green')
magenta = fg('magenta')
white = fg('white')

ascii_banner = pyfiglet.figlet_format("PSSWD MNGR")


class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self. password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]
    
def main():
    password = {
        "email": "1234567",
        "facebook": "passwdface",
        "youtube": "asdasdasd123",
        "something": "valamivalami_234"
    }

    pm = PasswordManager()

    print(magenta + ascii_banner)

    print(white + "-" * 50)
    print(magenta + 'Made with <3 Bujdosone Kovacs Brigi')
    print(white + "Started at: " + str(datetime.now()))
    print(white + "-" * 50)
    print(white + "\n")

    print(white + """What do you want to do?
    [1] Create a new key
    [2] Load an existing key
    [3] Create new password file
    [4] Load existing password file
    [5] Add a new password
    [6] Get a password
    [q] Quit
    """)

    done = False

    while not done:

        choice = input(blue + "[*] Enter your choice: ")
        if choice == "1":
            path = input(blue + "[*] Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input(blue + "[*] Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input(blue + "[*] Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input(blue + "[*] Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input(blue + "[*] Enter the site: ")
            password = input(blue + "[*] Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input(blue + "[*] What site do you want: ")   
            print(green + f"[+] Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print(magenta + "[X] Quit ")
            print(white + "\n")
        else:
            print(red + "[!] Invalid choice!")

if __name__ == "__main__":
    main()

