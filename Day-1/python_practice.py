#reverse a string
name="Sowmya"
rev="".join(reversed(name))
print(rev)


#count vowels in a sentence
sentence="the sun rises in the east"
vowels="aeiouAEIOU"
count=0
for i in sentence:
    if i in vowels:
        count+=1
print(count)


#fint the largest number in a list
list1=[19,90,60,70,40,90]
print(max(list1))
