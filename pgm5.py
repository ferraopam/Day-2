"""Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use map method.)
Example:
Input:
x = [1,2,3,4]
y = [5,6,7,8]
Output: 
z = [6,8,10,12]"""

list_1 = [2,3,4,5] 
list_2 = [2,1,3,4]
res = list(map(lambda x,y:x + y,list_1,list_2))
print(res)	
