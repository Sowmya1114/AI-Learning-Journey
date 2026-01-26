# Day-5 DSA Interview Practice

nums = [1,2,3,2,4,5,1,6]

# Frequency count
freq = {}
for n in nums:
    freq[n] = freq.get(n,0)+1
print("Frequency:", freq)

# Find duplicates
duplicates = [k for k,v in freq.items() if v > 1]
print("Duplicates:", duplicates)

# Remove duplicates
unique = list(set(nums))
print("Unique List:", unique)
