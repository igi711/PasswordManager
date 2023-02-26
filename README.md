# PasswordManager
***
## Contents of this file
***
- Introduction
- Requirements
- Maintainers

## Introduction
***
This is a Password Manager in Python with criptography Fernet.

Open Terminal in PasswordManager directory, and write : 
```
$python PasswordManager.py
```
This will launch in the terminal and you will see the following:

![PasswordManager](https://github.com/igi711/PasswordManager/blob/main/passwdmngr.png)

### Examples of how it works:
***

**Create password**
---
```
Enter your choice: 1                    // create a new key
Enter path: mykey.key                   // name of a new key
Enter your choice: 3                    // Create new password file
Enter path: passwd.pass                 // name of a new password file
Enter your choice: 5                    // Add a new password
Enter the site: example                 // enter name of site
Enter the password: passwd123           // enter your password for site
Enter your choice: 6                    // Get a password
What site do you want: example          // name of a site
Password for example is passwd123       // your password 
Enter your choice: q                    // Quit
```

**Get a password**
---
``` 
Enter your choice: 2                    // Load an existing key
Enter path: mykey.key                   // enter name of your key
Enter your choice: 4                    // Load existing password file
Enter path: passwd.pass                 // enter name of your password file
Enter your choice: 6                    // Get a password
What site do you want: example          // name of a site
Password for example is passwd123       // your password
Enter your choice:q                     // Quit
```

## Requirements
***
This module requires the following modules:

- [Python](https://docs.python.org/3/)
- [Cryptography](https://pypi.org/project/cryptography/)
- [Pyfiglet](https://pypi.org/project/pyfiglet/)
- [Colored](https://pypi.org/project/colored/)

## Maintainers
***
- Brigitta Bujdosone Kovacs - [kovacsbrigi.hu](https://kovacsbrigi.hu/)


