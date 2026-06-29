// Find the largest number in a list
num=[20,43,55,12,43,65,3,2,1]
max=num[0]
for i in num:
    if i>max:
        max=i
print("the max num is ",max)        


// Find the 2nd largest number in a list
num=[10,20,43,21,54,65,1]
num.sort()
print(num)
print("the  largest num is",num[-1])
print("The second largest num is :",num[-2])

// Remove duplicate values from a list.
list=[21,43,32,21,43,32,54]
print(list)
newlist=set(list)
print(newlist)


// Reverse a list without using built-in reverse()
num=[20,43,55,12,43,65,3,2,1]
for i in range(len(num)-1,-1,-1):
    print(num[i])

// Find common elements between two lists.
num1 = [10, 20, 30, 40, 50]
num2 = [30, 40, 60, 70]
common = set(num1) & set(num2)
print(common)

