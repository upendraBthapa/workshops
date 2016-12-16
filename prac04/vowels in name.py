__author__ = 'jc449735'
name = input("enter your lovely yet sarcastic and ironic name: ")
vowels = ["a","e","i","o","u"]
vowel=0
for char in name:
    if char.lower() in vowels:
        vowel += 1

#print(vowel)
print("Out of {} letters, {} has {} vowels".format(len(name),name,vowel))
