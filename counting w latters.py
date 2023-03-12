import string
print("input a number between 0-26 ")
num=int(input())


# Create an empty array to hold the letters
letters = []

# Loop through all the uppercase and lowercase letters in English
for i in string.ascii_lowercase:
    # Add each letter to the array
    letters.append(i)
# Print the array

if num < 0 or num >26:
    print("not valid number")
else:
    for i in range(num):
        print(letters[i], end = '-')

