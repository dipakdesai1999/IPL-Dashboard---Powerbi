def is_palindrome(s):

    s = s.lower() 
    return s == s[::-1]


test_string = "Madam"
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")
