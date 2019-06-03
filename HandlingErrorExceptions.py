
# coding: utf-8

# In[1]:


for i in ['a', 'b', 'c']:
    print(i**2)


# In[3]:


try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print('The List consist of strings')
    


# In[5]:


try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print('Cannot be divisible by Zero')
finally:
    print('All Done')


# In[ ]:






# In[9]:


def ask():
    waiting = True
    while waiting:
        try:
            number = 0
            number = int(input('Write a number here: '))
        except ValueError:
            print('You didnt input a correct number')
            break
        else:
            a = number**2
            print('{} is the square of your number, {}'.format(a, number))
        finally:
            print('Thank You')


# In[10]:


ask()

