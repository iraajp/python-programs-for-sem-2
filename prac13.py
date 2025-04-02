import re

# Function to validate phone number
def validate_phone_number(phone_number):
    # Regular expression for phone number (simple format: (xxx) xxx-xxxx or xxx-xxx-xxxx)
    phone_pattern = r"^\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{4}$"
    if re.match(phone_pattern, phone_number):
        return True
    return False

# Function to validate email address
def validate_email(email):
    # Regular expression for email address
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email):
        return True
    return False

# Prompt user for phone number and email ID
phone_number = input("Enter your phone number (e.g., (123) 456-7890 or 123-456-7890): ")
email = input("Enter your email ID: ")

# Validate the inputs
if validate_phone_number(phone_number):
    print("Phone number is valid.")
else:
    print("Invalid phone number format.")

if validate_email(email):
    print("Email address is valid.")
else:
    print("Invalid email address format.")
