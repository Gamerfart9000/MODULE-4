#1

n = int(input("Enter a number: "))
odd = [i for i in range(1, n) if i % 2 != 0]
another_odd = [11, 13, 15]

combined_list = odd + another_odd

print("Odd numbers below", n, ":", odd)
print("Combined list:", combined_list)

#2

fruits = ["apple", "banana", "cherry", "mango", "orange"]
capital = []

for i in fruits:
    capital.append(i[0].upper())

print(capital)