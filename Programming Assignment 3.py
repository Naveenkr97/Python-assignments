#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?


# In[2]:


number = int(input('Enter the number'))
if number>0:
    print('Positive number')
elif number ==0:
    print('Zero')
else:
    print('Negative number')


# In[ ]:


#2.	Write a Python Program to Check if a Number is Odd or Even?


# In[3]:


number = int(input('Enter the number'))
if number%2==0:
    print("Even number")
else:
    print("Odd number")


# In[ ]:


#3.	Write a Python Program to Check Leap Year?


# In[2]:


year = int(input("Enter the year"))

if year%100 ==0:
    if year%400 ==0:
        print('Leap year')
    else:
        print('Not a leap year')
else:
    if year%4 ==0:
        print('Leap year')
    else:
        print('Not a leap year')


# In[ ]:


#4.	Write a Python Program to Check Prime Number?


# In[19]:


number = int(input('Enter the number'))
indicator=0
for i in range(2,number):
    if number%i ==0:
        indicator = indicator+1
        break;
if indicator==0:
    print('Prime Number')
else:
    print('Not a prime number')
         
        


# In[ ]:


#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?


# In[18]:


indicator=0
for j in range(2,10001):
    for i in range(2,j):
        if j%i==0:
            indicator= indicator+1
    if indicator==0:
        print(j)
    else:
        indicator=0


# In[ ]:




