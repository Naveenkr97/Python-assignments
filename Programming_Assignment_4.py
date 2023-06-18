#!/usr/bin/env python
# coding: utf-8

# # 1.Write a Python Program to Find the Factorial of a Number?

# In[5]:


number = int(input("Enter the number: "))
print("Factorials of number are : ")
for i in range(1,number+1):
    if number%i == 0:
        print(i)


# # 2.Write a Python Program to Display the multiplication Table?

# In[6]:


number = int(input("Enter the number: "))
print("Multiplication table of number : ")
for i in range(1,11):
    print("{}*{}={}".format(number,i,number*i))


# # 3.Write a Python Program to Print the Fibonacci sequence?

# In[8]:


def fibonacci_sequence(n):
    a,b= 0,1
    sequence=[]
    
    while len(sequence)<n:
        sequence.append(a)
        a,b=b,a+b
        
    return sequence

number = int(input("Enter the number of terms"))

for i in fibonacci_sequence(number):
    print(i,end=" ")
         


# # 4.Write a Python Program to Check Armstrong Number?

# In[3]:


n = input("enter the number: ")
b = 0
for i in range(len(n)):
    b= b+ (int(n[i])**3)
if b == int(n):
    print("The number {} is an Armstrong number".format(n))
else:
    print("The number {} is not an Armstrong number".format(n))


# # 5.Write a Python Program to Find Armstrong Number in an Interval?

# In[12]:


a = input("Enter the intial value of the interval: ")
b = input("Enter the final value of the interval: ")
c = 0
print("The armstrong number in an interval ({},{}) are:".format(a,b))
for i in range(int(a),int(b)+1):
    for j in range(len(str(i))):
        c=c+(int(str(i)[j])**3)
    if c ==i:
        print(i)
        c=0
    else:
        c=0


# # 6.Write a Python Program to Find the Sum of Natural Numbers?

# In[16]:


n = int(input("Enter the number"))
b = 0
if n<1:
    print("Enter a natural number")
else:
    for i in range(1,n+1):
        b= b+i
    print("The sum of natural number is",b)


# In[ ]:




