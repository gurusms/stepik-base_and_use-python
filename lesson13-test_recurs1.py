def listSum(ls):
     # Base condition
     if not ls:
         return 0

     # First element + result of calling `listsum` with rest of the elements
     return ls[0] + listSum(ls[1:])
 
print(listSum([1, 3, 4, 5, 6]))