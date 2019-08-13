
# coding: utf-8

# In[124]:


# 1: Write a Python program to input a number from the user and check if it is positive, negative or zero. 
numb=int(input("Enter a number: "))
print("Entered number is",numb)
if (numb==0):
    print ("Entered Number is Zero. Please Enter another number")
elif (numb<0):
    print ("Entered Number is an Negative Number:",numb)
else:
    print ("Entered Number is an Positive Number:",numb)


# In[135]:


# 2: Write a Python Program to Check if a Number is Odd or Even by taking user input. 
numb=int(input("Enter a number: "))
print("Entered number is",numb)
if (numb==0):
    print ("Entered Number is = 0",numb)
elif (numb%2==0):
    print ("Entered Number is an Even Number:",numb)
else:
    print ("Entered Number is an Odd Number:",numb)


# In[179]:


# 3: Write a Python Program to input a year with century and 
#check if it is Leap Year or 
#print invalid if it is not in the form of year with century. 

Year = int(input("Enter start year: "))
if(Year%400==0)or((Year%4==0)and(Year!=0)):
    print (Year, "is a Leap Year")
else:
    print (Year, "is not a Leap Year")



# In[200]:


# 4a: Write a Python Program to Find the Largest Among Three Numbers, using the least number of lines of code. 
#.split() is a function used to provide a gap/space between the numbers entered
a,b,c = input("Enter 3 Numbers:").split()
print("Entered number 1 is: ",a)
print("Entered number 2 is: ",b)
print("Entered number 3 is: ",c)
if(a>b)and(a>c):
    print("Entered Number:",a,"is Biggest")
elif(b>a)and(b>c):
    print("Entered Number:",b,"is Biggest")
else:
    print("Entered Number:",c,"is Biggest")


# In[143]:


# 4b : Write a Python Program to Find the Largest Among Three Numbers, using the least number of lines of code. 
#.split() is a function used to provide a gap/space between the numbers entered
a,b,c = input("Enter 3 Numbers:").split()
print("Entered number 1 is: ",a)
print("Entered number 2 is: ",b)
print("Entered number 3 is: ",c)

if((0<int(a))and(0<int(b))and(0<int(c))):
    if(a>b)and(a>c):
        print("Entered Number:",a,"is Greatest")
    elif(b>a)and(b>c):
        print("Entered Number:",b,"is Greatest")
    else:
        print("Entered Number:",c,"is Greatest")
else:
    print("Please Enter 3 Positive Numbers")


# In[162]:


#Write a Python Program to Check if a number is Prime Number or not.

numb=input("Please enter a positive number")
print("Entered Number is:", numb)
if (numb>1):
    for i in range(2,int(numb)):
        if (int(numb)%i==0):
            print(numb,"Is not a prime Number")
            break
        else:
            print(numb,"Is a prime Number")
            print(numb)


# In[128]:


numb=int(input("Enter a number: "))
#print("Entered number is",numb)
if (numb==0):
    print ("Number is Zero")
elif (numb<0):
    print ("Negative Number")
else:
    print ("Positive Number")


# In[196]:


# 5 : Write a Python program to input a month name and print number of days in it. 
#Eg., January – 31 
#February – 28/29 
mon1=("Jan","Mar","May","Jul","Aug","Oct","Dec")
mon2=("Apr","June","Sept","Nov")
mon3=("Feb")
month=input ("Enter Month:")
print(month)
if (month in mon1):
    print ("31 days")
elif (month in mon2):
    print ("30 days")
else:
    print ("28 Days")


# In[194]:


import datetime
y=2022
x = datetime.datetime.y()

print(x.strftime("%j"))


# In[205]:


timedate = "2002"
print ("Length of the string: ", len(timedate))


# In[215]:


import calendar 
print (366)
if calendar.isleap(2019):
     365 


# In[255]:


import datetime 
#year = 2020 
year=input("Enter a Year")
d1 = datetime.date(int(year), 1, 1) 
d2 = datetime.date(int(year) + 1, 1, 1) 
d3=(d2 - d1)
if((d2 - d1)!=d3):
    print ("Leap Year")
else:
    print ("Not Leap year")

