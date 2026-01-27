# Reverse a list
nums = [1, 2, 3, 4, 5]
print("Reversed List:", nums[::-1])

# Second largest number
nums2 = [10, 50, 20, 80, 60]
nums2.sort()
print("Second Largest:", nums2[-2])

# Palindrome check
def is_palindrome(s):
    return s == s[::-1]

print("Is 'madam' palindrome?", is_palindrome("madam"))
