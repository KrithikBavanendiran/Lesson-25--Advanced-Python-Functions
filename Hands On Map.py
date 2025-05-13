numbers1=[1,2,3]
numbers2=[4,5,6]
result=map(lambda x,y:x+y,numbers1,numbers2)
print("Addition of 2 lists: ",list(result))

numbers3=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq,numbers3))

print(square)
