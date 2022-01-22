import pdb
import csv
import mysql.connector

starting_value = int(input("Enter starting value: "))
ending_value = int(input("Enter ending value: "))

for i in range(starting_value, ending_value + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")


mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='mohit'
)


def main():
    query = " "
    cursor = mydb.cursor()
    cursor.execute(query)
    pass


with open('', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for lines in csv_reader:
        pass


def up_low(s):
    upper_count = 0
    lower_letter = 0
    for letters in s:
        if letters.isupper():
            upper_count = upper_count+1
        elif letters.islower():
            lower_letter += 1

    print(f"Upper case letters are {upper_count}")
    print(f"lower case letters are {lower_letter}")


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


a = [1, 2, 3]
x = 2
y = 3

print(a)
print(x+y)

pdb.set_trace()    # Debugging tool
print(a+x)
