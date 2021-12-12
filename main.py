import random
from database import insert_into_database, select_from_database


# Check password
def check_password():
    password = input('Enter your password: ')

    # Check if password is at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return
    
    # Check if password contains letter
    if not any(char.isalpha() for char in password):
        print("Password must contain letters")
        return
    
    # Check if password contains at least one number
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number")
        return
    
    # Check if password contains at least one special character
    if not any(char in '!@#$%^&*()_+' for char in password):
        print("Password must contain at least one special character")
        return
        
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter")
        return
    
    print(f'\nYour password is: {password}\n')
    ask_about_database(password) 
    

def generate_password(length):
    # Generate a random password
    password = ''
    for i in range(length):
        password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+')
        
    return password


def main():
    print_menu()
    
    option = int(input('Enter your option: '))
    
    if option == 1:
        length = int(input('Enter a length for the new password: '))
        if length < 8:
            print("Password must be at least 8 characters long")
            return
        
        password = generate_password(length)
        print(f'\nYour new password is: {password}\n')
        ask_about_database(password)    
    
    elif option == 2:
        check_password()
    
    elif option == 3:
        select_from_database()
        
    else:
        print('Goodbye!')
        quit()
    
    string = input('Anything else? (y/n): ')
    print('')
    if string in 'yY':
        main()
    else:
        print('Goodbye!')
        quit()
    
    print('Thanks for using this program!')
        
    
def print_menu():
    print('1. Generate a new password')
    print('2. Check password')
    print('3. See all passwords')
    print('4. Quit')    
    

def ask_about_database(password):
    print('Would you like to add your new password to the database?')
    print('1. Yes')
    print('2. No')
    
    ask = int(input('> '))
    
    if ask == 1:
        insert_into_database(password)
            
    else:
        print('Goodbye!\n')
        quit()
        

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nYou pressed Ctrl+C or Delete to exit')
        quit()