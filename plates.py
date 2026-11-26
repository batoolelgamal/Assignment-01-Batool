def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Minimum 2 and maximum 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Only letters and numbers are allowed
    if not s.isalnum():
        return False

    # Numbers must come at the end
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False

    return True


main()
