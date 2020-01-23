"""
Instructions:

The ISBN-10 verification process is used to validate book identification numbers. These normally contain dashes and look like: 3-598-21508-8
ISBN
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:
(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.
"""

def is_valid(isbn):
    new_isbn = isbn.replace("-", "")
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X"]
    if not len(new_isbn) == 10:
        return False
    for i in new_isbn:
        if i not in chars:
            return False
    else:
        calc = 0
        index = 10
        for i in new_isbn:
            if i == "X":
                if not new_isbn.find(i) == 9:
                    return False
                else:
                    calc += 10 * index
                    index += -1
            else:
                calc += int(i) * index
                index += -1
        if calc % 11 == 0:
            return True
        else:
            return False
