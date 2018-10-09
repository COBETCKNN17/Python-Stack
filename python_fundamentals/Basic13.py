def print1to255():
  #Jessica
  for i in range(256): 
    print(i)

#print1to255()

def printOdd1to255():
  #Phil
  for i in range(1,256,2):
    print(i)
  return

#printOdd1to255()

def printIntsAndSum255():
  #Rudolph
  sum =0
  for i in range(1,256):
    print(i)
    sum+=i
  print(sum)

#printIntsAndSum255()
  
def printArrayVals(arr):
  #Jessica
  for i in arr:
    print (i)

#printArrayVals([2,5,7,8,5,6,4,3,5,6,4])

def printMax(arr):
  #Phil
  max=arr[0]
  for thing in arr:
    if(thing>max):
      max=thing
  print(max)

#printMax([1,20,2,3,4])

def printAvg(Arr):
  #Rudolph
  sum = 0
  for i in Arr:
    sum+=i
  print(sum/len(Arr))

#a = [3,3]
#printAvg(a)

def returnOddsArr():
  #Jessica
  banana = []
  for i in range(1,256,2):
    banana.append(i)
    #append in py is just like push in js
  print(banana)
  return

#returnOddsArr()

def squareVals(arr):
  #Phil
  for i in range(len(arr)):
    arr[i]=arr[i]*arr[i]
  return arr

#print(squareVals([1,2,3,4]))

def gtrThanY(arr, y):
  #Rudolph
  count = 0
  for i in arr:
    if i> y:
      count+=1
  return count

#print(gtrThanY([200,5,4,6,300,120,100.00001], 100))

def zeroOutNegatives(arr):
  #Jessica
  for i in range(len(arr)):
    if arr[i] < 0:
     arr[i] = 0 
  print(arr)
  return arr

#zeroOutNegatives([5,6,-8,-9,0])

def printMinMaxAvgOfArr(arr):
  #Phil
  sum=0
  min=arr[0]
  max=arr[0]
  for i in range (len(arr)):
    sum+=arr[i]
    if(arr[i]>max):
      max=arr[i]
    if(arr[i]<min):
      min=arr[i]
  print(min,max,sum/len(arr))

#printMinMaxAvgOfArr([1,2,3,4])

def leftShift(arr):
  #Rudolph
  arr = arr[1:]+[0]
  return arr
  #plus sign adds the two arrays together, like a print
  #colon operator is a range selector (like arr.slice in JS)

#print(leftShift([1,2,3,4]))

def leftShift2(arr):
  for i in range(len(arr)-1):
    arr[i] = arr[i+1]
  arr[len(arr)-1] = 0
  print(arr)
  return arr

#leftShift2([1,2,3])

def swapNegativesForString(arr):
  for i in range(len(arr)):
    if arr[i] < 0:
     arr[i] = "Dojo"
  print(arr)
  return arr

#swapNegativesForString([-1,2,3,4,-10])