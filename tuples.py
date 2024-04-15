numbers =1,2,3,4,5,6
print(numbers)

#accessing values in a tuple
print(numbers[3])
print(numbers[-1])

#to add new tuple to a tuple
numbers = numbers + (8,)
print(numbers)

#to be able to vreate another tuple from two tuples
number = (1,2,3,4) + (5,6,7,8)
print(number)

#to slice a tuple
print(number[:-2])
print(number[3:5])

#for repition
new_numbers = numbers*3
print(new_numbers)

#for membership check
print(3 in number)
print(8 in number)
print(9 in number)

#to get the length of a tuple
print(len(number))

#to get the maximum element in a tuple.
print(max(number))

#to get the minimum number
print(min(number))

# delete a tuple
del (number)