'''
Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". 
Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
'''
def biggie_size(arr): 
    for i in range(len(arr)): 
        if(arr[i] > 0): 
            arr[i] = "big"
    return arr

print(biggie_size([-1,-2,-3,4,5,-3]))

'''
Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. 
Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
'''
def count_positives(arr): 
    sum = 0
    for i in range(len(arr)): 
        sum += arr[i]
    arr[len(arr)-1] = sum
    return arr 

print(count_positives([4,5,6]))

''' SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  
For example sumTotal([1,2,3,4]) should return 10
'''
def sum_total(arr): 
    return sum(arr)

print("sum total",sum_total([4,5,6,7]))

'''
Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  
For example multiples([1,2,3,4]) should return 2.5
'''
def average(arr): 
    sum = 0 
    for i in range(len(arr)): 
        sum += arr[i]
    return (sum / len(arr))

print(average([4,5,7,75,4]))

'''
Length - Create a function that takes an array as an argument and returns the length of the array.  
For example length([1,2,3,4]) should return 4'''
def length(arr): 
    return len(arr)

print(length([3,4,5,1,2]))

'''
Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  
If the passed array is empty, have the function return false.  
For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.'''
def minimum(arr): 
    return min(arr)

print("minimum of array", minimum([3,4,5]))

'''Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  
If the passed array is empty, have the function return false.  
For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
'''
def maximum(arr): 
    if(len(arr) == 0): 
        return false
    else: 
        return max(arr)

print("maximum is", maximum([4,5,6]))

'''
UltimateAnalyze - Create a function that takes an array as an argument and 
returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.'''
def ultimate_analyze(arr): 
    dict = {}
    dict['sumTotal'] = sum(arr)
    dict['average'] = sum(arr) / len(arr)
    dict['minimum'] = min(arr)
    dict['maximum'] = max(arr)
    return dict

print(ultimate_analyze([4,4,5,6,7,8]))

'''
ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  
Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. 
This challenge is known to appear during basic technical interviews.'''
def reverse_list(arr): 
    for i in range(len(arr)-1,0,-1): 
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
    return arr

print(reverse_list([1,4,5])) 