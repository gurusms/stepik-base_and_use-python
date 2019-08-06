# http://qaru.site/questions/333113/basics-of-recursion-in-python
def listSum(ls, result):
     if not ls:
        return result
     return listSum(ls[1:], result + ls[0])
 
print(listSum([1, 3, 4, 5, 6], 0))