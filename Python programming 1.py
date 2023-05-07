#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print "Hello Python"?

# In[3]:


print("Hello Python")


# In[5]:


#2.	Write a Python program to do arithmetical operations addition and division?


# In[9]:


a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print('The sum of two numbers',a+b)
print('The divison of two numbers',b/a)


# In[11]:


#3.	Write a Python program to find the area of a triangle?


# In[23]:


a = int(input("Enter the length of the first side of the traingle"))
b = int(input("Enter the length of the second side of the traingle"))
c = int(input("Enter the length of the third of the traingle"))
s = (a+b+c)/2  
print('The area of triangle is',round((s*(s-a)*(s-b)*(s-c))**0.5,2))


# In[17]:


print(4**0.5)


# In[ ]:


#4.	Write a Python program to swap two variables?


# In[25]:


x = int(input('Enter a number'))
y = int(input('Enter a number'))
temp = x
x = y
y = temp
print('New value of x',x)
print('New value of y',y)


# In[26]:


#5.	Write a Python program to generate a random number?


# In[27]:


import random

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# Print the random number
print("Random number:", random_number)


# In[ ]:




