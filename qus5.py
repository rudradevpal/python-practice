"""
Qus 5. Given a positive integer, return its corresponding column title as appear in an Excel sheet.
Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words,
column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.
"""


# Method 1
def convert_to_title(column_number):
    title = []

    while column_number > 0:
        # Adjust for zero-based indexing
        column_number -= 1

        # Get the remainder and convert it to a character
        remainder = column_number % 26
        title.append(chr(remainder + ord('A')))

        # Move to the next digit
        column_number //= 26

    # Reverse the list to get the correct order
    return ''.join(reversed(title))


# Example usage
print(convert_to_title(28))  # Output: "AB"