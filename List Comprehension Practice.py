numbers=[1,2,3,4,5,6,7,8,9]
print("First list of numbers:", numbers)
odd= [i for i in numbers if i%2==0]
print("The new list of odd numbers: ",odd)


fruits=["apple", "pear", "banana"]
upper_fruits= [i.capitalize() for i in fruits]
print(upper_fruits)