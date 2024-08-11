import random

def Generate_password(length):
    """Generates a random password of the specified length."""
    Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    Password = ''.join(random.choice(Characters) for i in range(length))
    return Password

if __name__ == "__main__":
    password_len = int(input("Enter desired password length: "))
    Password = Generate_password(password_len)
    print("Generated password:", Password)
