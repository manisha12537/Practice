# a=int(input('enter num'))
# dic={}
# i=0
# while i<=(a):
#     b=input("enter the name")
#     dic[i]=b
#     i+=1
# print(dic)


def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1+v1==x2+v2:
        print("YES")
    else:
        print("NO")
kangaroo(0,3,4,2)