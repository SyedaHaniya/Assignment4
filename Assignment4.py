#!/usr/bin/env python
# coding: utf-8

# In[1]:


dic = {'first_name': "Haniya", 'last_name': "Zehra", 'age': 19, 'city': "Karachi"}
print (dic)
dic['qualification'] = "high academic level"
print ("After addition")
print (dic)
del dic['qualification']
print ("After deletion")
print (dic)


# In[2]:


cities = {
    'Karachi': {'country': "Pakistan", 'population': "14.91 million", 'fact': "6th largest populated city in the world"},
    'Mumbai': {'country': "India", 'population': "18.41 million", 'fact': "Richest city of India"},
    'Siberia': {'country': "Russia", 'population': "36 million", 'fact': "One of the coldest countries in the world"}
}
print (cities)


# In[3]:


age = int (input("Enter your age: "))
if (age < 3):
    print ("Free ticket!")
elif (age >= 3 and age <= 12):
    print ("Ticket price is $10!")
elif (age > 12):
    print ("Ticket price is $15!")


# In[4]:


def favourite_book(Thumblina):
    print (Thumblina)
    return
favourite_book ("Thumblina is one of my favourite books!!!")


# In[8]:


import random
num = random.randrange(1, 30)

guess = int (input("Enter your guess: "))
if (guess == num):
    print ("\nYou guessed it right!!! The number was:")
    print (num)

elif (guess < num):
    print("You guessed it wrong")
    print("Hint: Number is greater than your guessed number")
    guess2 = int (input("Try again: "))
    if (guess2 == num):
        print ("\nYes...you guessed it right...The number was:")
        print (num)   
    
    elif (guess2 < num):
        print("You guessed it wrong again")
        print("Hint: Number is greater than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...The number was:")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was:")
            print (num)          
    
    elif (guess2 > num):
        print("You guessed it wrong again")
        print("Hint: Number is less than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...The number was:")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was:")
            print (num)

elif (guess > num):
    print("You guessed it wrong" )
    print("Hint: Number is less than your guessed number")
    guess2 = int (input("Try again: "))
    if (guess2 == num):
        print ("\nYes...you guessed it right...The number was:")
        print (num)
    
    elif (guess2 < num):
        print("You guessed it wrong again")
        print("Hint: Number is greater than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...The number was:")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was:")  
            print (num)
    
    elif (guess2 > num):
        print("You guessed it wrong again")
        print("Hint: Number is less than your guessed number")
        guess3 = int (input("Try again: "))
        if (guess3 != num):
            print("\nYou lost...The number was:")
            print (num)
        elif (guess3 == num):
            print("\nYou Won! The number was:")    
            print (num)


# In[ ]:




