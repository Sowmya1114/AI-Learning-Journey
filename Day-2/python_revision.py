# Factorial using function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print("Factorial of 5:", factorial(5))

# Word frequency using dictionary
sentence = "ai engineer ai learning journey"
words = sentence.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Word Frequency:", freq)
