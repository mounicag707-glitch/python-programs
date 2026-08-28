text = input("Enter a word: ")
count = 0
for char in text.lower():
    if char in "aeiou":
        count += 1
print("Vowels =", count)
