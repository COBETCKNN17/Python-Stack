'''
Countdown - Create a function that accepts a number as an input.  
Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  
For example countDown(5) should return [5,4,3,2,1,0].
'''

def contdown(num): 
    return list(range(num,-1, -1))

countdown(4) 

'''
Print and Return - Your function will receive an array with two numbers. 
Print the first value, and return the second.
'''

def print_and_return(num1, num2): 
    print(num1)
    return(num2)

print_and_return(3,4)

'''First Plus Length - Given an array, 
return the sum of the first value in the array plus the array's length.'''
def first_plus_length(arr): 
    sum = 0
    for i in arr:
        sum += i
    print(arr[0] + sum)

first_plus_length([2,4,5,7,8])

'''Values Greater than Second - Write a function that accepts any array, 
and returns a new array with the array values that are greater than its 2nd value.  
Print how many values this is.  If the array is only one element long, have the function return False'''
def values_greater_than_second(arr): 
    newArr = []
    if(len(arr) == 1):
        return False 
    for i in range(len(arr)): 
        if(arr[i] > arr[1]): 
            newArr.append(arr[i])
    print("newArr", newArr)
    print("Therea are {} items greater than the second element of the array".format(len(newArr)))

values_greater_than_second([5,4,56,6])

'''
This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. 
This function should take two numbers and return a list of length size containing only the number in value. 
For example, lengthAndValue(4,7) should return [7,7,7,7].
'''
def lengthAndValue(size, value): 
    newArray = []
    for i in range(size): 
        newArray.append(value) 
    return newArray 

print(lengthAndValue(4,7)) 

