def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

text = input("Enter a string: ")
print(f"Is palindrome: {is_palindrome(text)}")