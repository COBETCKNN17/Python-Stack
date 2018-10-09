#Given
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print("x", x)

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
students[0]['last_name'] = 'Bryant' 

print(students) 

# For the sports_directory, how would you change 'Messi' to 'Andres'?
sports_directory['soccer'][0] = 'Andres'
print(sports_directory) 

# For z, how would you change the value 20 to 30?
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30 

# Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  
# For example, given the following list:
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def loop(students): 
    for i in students: 
      for k,v in i.items():
          print(k, '-', v)

print(loop(students)) 

# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  
# For example, iterateDictionary2('first_name', students) should output
def number_three(list_of_dictionaries): 
    for i in list_of_dictionaries: 
        for k,v in i.items():
            if(k=='first_name'): 
                print(v)

print(number_three(students))

#4
dojo_list = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def dojo_count(dojo_list): 
    for i,v in dojo_list.items(): 
      print(i)
      for x in v: 
        print(x)

print(dojo_count(dojo_list)) 
