Dic={"developer":{"count":2,"user":["anurag"]},"tester":{"count":2,"user":["jyoti","rohit"]}}
Dic_2={}
for i,j in Dic.items():
    for k in j:
        if(type(j[k])==list):
            Dic_2[i]=j[k]
print(Dic_2)