#python test
a=[]
b=[]
x=0
q="yes"
while (q=="yes"):
   a.append(input(f"please enter student name number {x+1} : "))
   b.append(input(f"please enter student id number {x+1}: "))
   q=input("do you want to add more students (yes/no)")
   ##print(q)
   while (q !="yes" and q!="no"):
        if (q !="yes" and q!="no"):
             q=input("please ansewr by yes or no only, do you want to add more students ? (yes/no)")
   x += 1
print("    Name            ID")
for x in range (len(a)):
#while(a[x] != 0):
    print(f"{x+1}- {a[x]}", end="    ")
    print(f"{b[x]}")