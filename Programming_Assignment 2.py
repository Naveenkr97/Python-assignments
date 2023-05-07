#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to convert kilometers to miles?


# In[4]:


dist = int(input('Enter the value in distance: '))
print('The value in miles is',round(dist*0.62137,2))


# In[5]:


#2.	Write a Python program to convert Celsius to Fahrenheit?


# In[8]:


celsius = int(input('Enter the value in celsius'))
print('The value in kelvin :', (9*celsius/5)+32)


# In[11]:


#3.	Write a Python program to display calendar?


# In[14]:


import calendar 

yy = int(input("Enter the year: "))
mm = int(input("Enter the month: "))

print(calendar.month(yy,mm))


# In[15]:


#4.	Write a Python program to solve quadratic equation?


# In[18]:


# Standard form of quadratic equation is ax2+bx+c = 0 
# x = -b+d/2a and x = -b-d/2a where d = (b**2 - 4ac)**0.5

a = int(input('Enter the value of coefficient of x square'))
b = int(input('Enter the value of coefficient of x '))
c = int(input('Enter the value of coefficient of constant'))

d = b**2 - 4*a*c
e = (-b+d**0.5)/2*a
f = (-b-d**0.5)/2*a

if d< 0:
    print('Real roots does not exist')
else:
    print('the solution of the quadratic equation are {} and {}'.format(e,f))
    
    


# In[ ]:


#5.	Write a Python program to swap two variables without temp variable?


# In[22]:


x = input('Enter value of x ')
y = input('Enter value of y ')
x,y = y,x
print('The swapped value of x and y are {} and {}'.format(x,y))


# In[ ]:




