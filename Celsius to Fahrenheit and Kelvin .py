
# coding: utf-8

# In[5]:


def celsius_to_fahrenheit():
    try:
        temp_c = 0
        temp_c = int(input('INPUT THE TEMPERATURE IN CELSIUS HERE: '))
        fahrenheit = int((9/5) * temp_c + 32 )
        kelvin = int(temp_c + 273.15)
        print('The value of {}°C is {}°F and {}K'.format(temp_c, fahrenheit, kelvin))
    except:
        print('YOU ARE ENTERING A WRONG VALUE, eg, try "20"')
    
    
    


# In[4]:


celsius_to_fahrenheit()

