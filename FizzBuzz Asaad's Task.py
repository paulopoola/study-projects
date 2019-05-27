#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fizzbuzz(x_list):
    #print number divisible by 3 as Fizz and divisible by 5 as Buzz, Divisible by both 3 and 5 and FizzBuzz. From 1~100
    for num in x_list:
        #where num represents the value from 1~100
        if num%3==0 and num%5==0:
            print(num,'FizzBuzz')
        elif num%3==0:
            print(num,'Fizz')
        elif num%5==0:
            print(num,'Buzz')
print(fizzbuzz(range(1,101)))


# In[ ]:





# In[ ]:




