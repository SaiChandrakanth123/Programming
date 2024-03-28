s=[]
a=input("Enter the string : ")
d={'(':1,'{':2,'[':3,')':-1,"}":-2,"]":-3}
for i in range(len(a)):
    if d[a[i]]>0:
        s.append(d[a[i]])
    else:
        if len(s)==0:
            print("Imbalance")
            break
        elif -(d[a[i]])==s[-1]:
            s.pop()
        else:
            print("Imbalance")
            break
else:
    print("balanced")
