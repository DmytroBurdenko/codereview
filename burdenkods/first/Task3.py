"""
2 float numbers: print list in range (num1, num2)
"""

lower_bound = int(input("Enter first number: "))
upper_bound = int(input("Enter second number: "))
if upper_bound >= lower_bound:
    for i in range(lower_bound, upper_bound + 1):
        print(i)
else:
    for i in range(upper_bound, lower_bound + 1):
        print(i)
