#!/usr/bin/env python
# coding: utf-8

# # 1.	Write a Python Program to Find LCM?

# In[ ]:


def find_lcm(a,b):
    max_num = max(a,b)
    lcm = max_num
    
    while True:
        if lcm%a ==0 and lcm%b == 0:
            break
        lcm = lcm+max_num
        
    return lcm

def find_lcm_multiple(numbers):
    if len(numbers)<2:
        print('Need at least 2 two numbers')
    lcm= numbers[0]
    for i in range(1,len(numbers)):
        lcm = find_lcm(lcm,numbers[i])

    return lcm

num_count = int(input("Enter the number of values: "))
num_list = []
for i in range(num_count):
    num = int(input(f"Enter value {i+1}: "))
    num_list.append(num)

# Calculate LCM
lcm = find_lcm_multiple(num_list)
print(f"The LCM of {num_list} is: {lcm}")


# # 2.Write a Python Program to Find HCF?

# In[2]:


def find_hcf(a,b):
    min_num = min(a,b)
    hcf = min_num
    
    while hcf>0:
        if a%hcf ==0 and b%hcf ==0:
            break
        hcf = hcf-1        
    return hcf

def find_hcf_multiple(numbers):
    if len(numbers)<2:
        print('Need at least 2 two numbers')
    hcf= numbers[0]
    for i in range(1,len(numbers)):
        hcf = find_hcf(hcf,numbers[i])

    return hcf

num_count = int(input("Enter the number of values: "))
num_list = []
for i in range(num_count):
    num = int(input(f"Enter value {i+1}: "))
    num_list.append(num)

# Calculate HCF
hcf = find_hcf_multiple(num_list)
print(f"The hcf of {num_list} is: {hcf}")

    


# # 3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

# In[5]:


num = int(input("Enter the number: "))
Bin = bin(num)
Octa = oct(num)
Hexa = hex(num)

print("Binary",Bin)
print("Octal",Octa)
print("Hexadecimal",Hexa)


# In[20]:


#Another solution 

number = int(input("Enter the number: "))

def dec_to_bin(number):
    bin = ""
    while number>0:
        bin = str(number%2)+bin
        #print(bin)
        number = number //2
        #print(number)
    return bin


def dec_to_oct(number):
    oct = ""
    while number>0:
        oct = str(number%8)+oct
        number = number //8
       
    return oct

def dec_to_hex(number):
    hex = ""
    hexa = "0123456789ABCDEF"
    while number>0:
        hex = str(hexa[number%16])+hex
        number = number //16
       
    return hex     

print("Binary","0b"+dec_to_bin(number))
print("Octal","0o"+dec_to_oct(number))
print("Hexadecimal","0x"+dec_to_hex(number))
   


# # 4.Write a Python Program To Find ASCII value of a character?

# In[21]:


character = input("Enter a character: ")

ascii_value = ord(character)  # Using the ord() function

print("ASCII value:", ascii_value)


# In[24]:


#Another solution

character = input("Enter a character: ")
a = None
for i in range(256):
    if chr(i) == character:
        a=i
        break
        
if a is not None:
    print("ASCII Value",a)
else:
    print("ASCII Not found")


# # 5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

# In[27]:


def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    result = add(num1, num2)
    operation = "+"
elif choice == '2':
    result = subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = multiply(num1, num2)
    operation = "*"
elif choice == '4':
    result = divide(num1, num2)
    operation = "/"
else:
    print("Invalid choice")
    exit()

print(f"{num1}{operation}{num2}={result}")


# In[ ]:




