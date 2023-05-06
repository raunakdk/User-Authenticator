import re
import random
import string


def authenticate_user():
    #  To Generate a random string of characters
    rand_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    print("Please type the following Captcha for Authentication: " + rand_string)

    user_input = input()

    # Compare user input to the generated strings
    if user_input == rand_string:
        print("Captcha Verified, Authentication successful! ")
    else:
        print("Invalid Captcha, Authentication failed.")

authenticate_user()


username = input("Enter your username: ")



valid_username = "RaunakDK"


#  Here we check if the entered credentials 
if username == valid_username:
    print("Username Authentication Successful, Username verified")
else:
    print("Authentication failed. Please check your credentials and try again.")
def check_password_strength(password):
    if len(password) < 8:
        return "Too short"
    if not re.search("[a-z]", password):
        return "No lowercase letter"
    if not re.search("[A-Z]", password):
        return "No uppercase letter"
    if not re.search("[0-9]", password):
        return "No digit"
    if not re.search("[@#$]", password):
        return "No special character"
    return "Strong"

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + "@#$"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = input("Enter a password: ")
print(check_password_strength(password))

generated_password = generate_password()
print("Here is the generated Strong Password that you can use- ", generated_password)
print(check_password_strength(generated_password))


#This script uses the random and string modules to generate a random string of 10 characters,
# consisting of both letters and digits. The input() function is used to ask the user to type the generated string,
# and their input is compared to the generated string using an if statement. If the input matches the generated string,
# the user is authenticated; otherwise, authentication fails





