# Day-6 DSA Practice

# Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print("Anagram check (listen, silent):", is_anagram("listen","silent"))

# Count vowels using function
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print("Vowel count:", count_vowels("AI Engineer"))

# Sum of digits
def sum_digits(n):
    return sum(int(d) for d in str(n))

print("Sum of digits of 1234:", sum_digits(1234))
