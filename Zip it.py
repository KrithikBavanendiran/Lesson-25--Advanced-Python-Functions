s1={2,3,1}
s2={'b','a','c'}
s3=list(zip(s1,s2))
print(s3)

list1=[5,3,8,2]
list2=[4,1,9,7]
for i,j in zip(list1,list2[::-1]):
    print(i,j)

stocks=["Apple","Samsung","Nvidia"]
prices=[2000,1000,3000]
new_dict={i:j for i,j in zip(stocks,prices)}
print(new_dict)