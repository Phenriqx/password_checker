import random

def main():
    
    # Get user input
    question = input("\nDo you want to create your own password or generate one automatically? (c/g) ")
    
    if question in ["c", "C"]:
        password = input("Enter your password: ")
        
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
        
        print("Your password is: " + password)
    
    else:
        try:
            length = int(input('Enter a length for the new password: '))
            
            if length < 8:
                print("\nPassword must be at least 8 characters long")
                return
            
            new_password = generate_password(length)
            print('Generating password... ')
            print('Your new password is: ' + new_password)
        
        except:
            raise Exception('Something went wrong!')
    
    print('Thanks for using this program!')
        
def generate_password(length):
    # Generate a random password
    password = ''
    for i in range(length):
        password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+')
        
    return password

if __name__ == "__main__":
    main()