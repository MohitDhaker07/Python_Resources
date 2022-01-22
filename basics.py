str = "print the words that starts with s in this sentence"

split_string = str.split()

for char in split_string:
    if char[0] == "s":
        print(char)

# range to print all the even number from 0 to 10

for even in range(0, 11, 2):
    print(even)

# if len for word is even print even

st = "print every word in the sentence that has even number of letters"

splitted_string = str.split(st)
even_words = []
for words in splitted_string:
    if len(words) % 2 == 0:
        even_words.append(words)

print(even_words)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # for sum of 3 number = given number 
user = int(input("Number: "))
for i in mylist:
    for j in mylist:
        for k in mylist:
            if (i + j + k) == user:
                print("Numbers are: ", i, j, k)
