def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    
    if not s[:2].isalpha():
        return False

    if not s.isalnum():
        return False

    found_number = False  
    for i, char in enumerate(s):
        if char.isdigit():
            if not found_number and char == '0':  # First number cannot be '0'
                return False
            found_number = True
        elif found_number:  # If a letter appears after a number, it's invalid
            return False

    return True

main()