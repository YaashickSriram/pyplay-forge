import re

class ValidationError(Exception):
    """ Raised when input fails validation """
    pass

def validate_email(email: str) -> bool:
    match_string = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(match_string, email):
        return True
    else:
        raise ValidationError(f"Invalid email: {email}")

def validate_phone_number(ph_number : str) -> bool:
    match_string = r"^\d{10}+$"
    if re.match(match_string, ph_number):
        return True
    else:
        raise ValidationError(f"Invalid phone number: {ph_number}")
    
if __name__ == "__main__":
    print(validate_email("yaashhiva@gmail.com"))
    print(validate_phone_number("9876543210"))

    try:
     validate_email("had@ds87")
    except Exception as e:
     print(f"Caught : {e}")

    try:
      validate_email("997")
    except Exception as e:
      print(f"Caught : {e}")
    
    try:
       validate_phone_number("670897")
    except ValidationError as e:
     print(f"Caught : {e}")

    try:
       validate_phone_number("7474645648750987897987")
    except ValidationError as e:
     print(f"Caught : {e}")