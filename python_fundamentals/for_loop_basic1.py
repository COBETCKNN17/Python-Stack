# Basic - print all the numbers from 0 to 150 
def basic():
	for i in range(0,150):
		print(i) 

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
def multiples_of_five():
	for i in range(5, 1000000):
		if(i%5 == 0): 
			print(i)

# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
def counting_dojo():
	for i in range(0,101):
		if(i % 10 == 0):
			print("Coding")
		elif(i % 5 == 0 and i % 10 != 0): 
			print("Dojo")
		else: 
			print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def huge(n):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
          print(i)
          sum = sum + i
    return sum

print (str(huge(500))) 

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
def countdown():
	for i in range(2018, 0, -4):
		print(i)

countdown()

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexibleCountdown(lowNum, highNum, mult):
	for i in range(lowNum, highNum, mult): 
		print(i) 

flexibleCountdown(1,40,3) 




















