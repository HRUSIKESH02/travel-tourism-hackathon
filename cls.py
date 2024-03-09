# a=input()
# for b in a:
#     c=a.index(b)
#     d=c+1
#     if d%2==0:
#         print(b.upper(),end="")
#     else:
#         print(b.lower(),end="")


# for i in range(10,0,-1):
#     print(i)

# num1=int(input("num:"))
# a=0
# b=1
# l=[0,1]
# print(a)
# print(b)
# for i in range(0,num1-2):
#     c=a+b
#     a=b
#     b=c
#     print(c)
#     l.append(c)
# print(l)


# num1=int(input("num1:"))
# l=[]
# for i in range(0,num1):
#     x=int(input())
#     l.append(x)
# print(l)
# s=0
# for j in l:
#     s=s+j
# print(s)


# l=[]
# for i in range(10,20):
#     continue
     
# for j in range(2,i):
#     if i%j!=0:
#         break
#     else:
#         print(i)
# # print(l)  


# for num in range(10,20):
   
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:


#             print(num)
#     #    else:
#     #        print(num)




# l=[]
# for i in range(10,20):
#     for j in range(2,i):
#         if i%j==0:
#             l.append(i)
# print(l)
# set1=set(l)
# print(set1)
# list1=list(set1)
# print(list1)
# tuple1=tuple(list1)
# print(tuple1)



# a=123
# b=repr(a)
# c=b.index("2")
# print(c)

# str1=input().split()
# for i in str1:
#     print(i[0])



# num=int(input())
# s=num**2
# st=repr(num)
# pt=repr(s)
# l=len(st)
# l1=0-l
# index=pt[:int(l1)-1:-1]
# ind=index[::-1]
# if st==ind:
#     print("automorphic")
# else:
#     print("none")


# num=int(input())
# st=repr(num)
# l=len(st)
# s=0
# for i in st:
#     s=s+int(i)**l
# if num==s:
#     print("armstrong")
# else:
#     print("none")


# s=0
# a=int(input())
# s=0
# p=1
# while a>0:
#     b=a%10
#     p=1
#     for i in range(1,b+1):
#         p=p*i
#     s=s+p
#     a=a//10
# print(s)
# a=int(input())
# st=repr(a)
# s=0
# for i in st:
#     p=1
#     for j in range(1,int(i)+1):
#         p=p*j
#     s=s+p
# print(s)


# tuple1=input().split(",")
# tuple2=input().split(",")
# list1=list(tuple1)
# list2=list(tuple2)
# dict1=dict(zip(list1,list2))
# print(dict1)
# set1=set(dict1)
# print(sorted(set1))


 

# l=[]
# num1=int(input("1:"))
# num2=int(input("2:"))
# while num1<=num2:
#     s=0
#     num1=num1+1
#     for i in range(1,num1):
#         if num1%i==0:
#             s=s+i
#     if s==num1:
#         l.append(num1)
# print(l)



# s=0
# num=int(input())
# for i in range(1,num):
#     if num%i==0:
#         # print(i)
#         s=s+i
# if s==num:
#     print("perfect")
# else:
#     print("not")


# l=[]
# num1=int(input())
# num2=int(input())
# for i in range(num1,num2):
#     # if i>0:
#     for j in range(2,i):
#         if i%j==0:
#             break
#         else:
#             l.append(i)
# print(l)

# l=["1",'2',]
# l1=list((map(int,l)))
# print(l1)
# print(max(l1))

# l=[]
# str1=input().split(" ")
# str2=input()
# for i in str1:
#     if i == str2:
#         l.append(i)
# print(len(l))


# list1=input().split(" ")
# l=[]
# for i in list1:
#     l.append(i)
# list2=list(map(int,l))
# for i in list2:
    
 
# num1=int(input())
# x,y=0,1
# print("0")
# while y<num1:
#     print(y,end=",")
#     x,y=y,x+y
#     # print(y)

# num1=int(input())
# print("0")
# print("1")
# x=0
# y=1
# for i in range(5):
#     z=x+y
#     x=y
#     y=z
#     print(z)


# num1=int(input())
# num2=int(input())
# a=num1
# b=num2
# if num2==0 or num1==0:
#     print("none")
# else:
#     while num2!=0:
#         b=num2
#         num2=num1%num2
#         num1=b
#         gcd=num1
#     print(gcd)

# l=[]
# num1=int(input())
# str1=str(num1)
# for i in str1:
#     l.append(i)
# l=list(map(int,l))
# print(l)
# print(sum(l))

# s=0
# num1=int(input())
# str1=repr(num1)
# for i in str1:
#     p=1
#     for j in range(1,int(i)+1):
#         p=p*j
#     s=s+p
    
# if s==num1:
#     print("strong")
# else:
#     print("none")


# l=[]
# s=0
# num1=int(input())
# num2=int(input())
# for i in range(num1,num2):
#     s=0
    
#     st=repr(i)
#     for j in st:
#         p=1
#         for k in range(1,int(j)+1):
#             p=p*k
#         s=s+p
#     if i==s:
#         l.append(i)
# print(l)

# str1=input()
# a=str1[:-4:-1]
# b=a[::-1]
# print(str1[:3]*2+b*3+str1[::-1])

# n=int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     c=1
#     for j in range(1,i+1):
#         print("",c,end="")
#         c=c*(i-j)//j
#     print("")

# n=int(input())
# for i in range(n):
#     l=[]
#     c=1
#     for j in range(1,i+2):
#         l.append(c)
#         c=c*(i-j+1)//j
#     print(l)

# n=int(input())
# for i in range(1,n+1):
#     a=1
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a=a+1
#     print(" ")

# a="abcdefghijklmnopqrstuvwxyz"

# n=int(input())
# for i in a:
#     b=a.index(i)
#     for i in range(1,n+1):
#         for k in range(1,i+1):
#             print(a[int(b)],end=" ")
#             b=b+1
        
#             if b>n:
#                 break
#         print()


# l=input().split(",")
# l1=list(map(int,l))
# m=[]
# for i in l1:
#     if i%2==0:
#         m.append("*")
#     else:
#         m.append(i)
# print(m)
# def prime(x):
    
#     for k in range(2,x):
#         if x%k==0:
#             return False
#         else:
#             return True
# prime(i)
# kk=[]
# for i in l1:
#     if j%2!=0 and prime(i) is True:
#         kk.append("*")
#     else:
#         kk.append(i)



# f=open("form.py","w")
# a=int(input())
# b=int(input())
# print()

