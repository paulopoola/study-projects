
# coding: utf-8

# In[ ]:


'''
THIS FUNCTION TAKES IN AN INTEGER INPUT IF ITS DIVISIBLE BY BOTH 3 AND 5 RETURNS FIZZBUZZ
IF ITS DIVISIBLE ONLY BY 3 RETURNS FIZZ
IF ITS DIVISIBLE ONLY BY 5 RETURNS BUZZ
IF ITS NOT DIVISIBLE BY EITHIER IT RETURNS 'NOT DIVISIBLE BY EITHIER 3 AND 5'

'''
def FizzBuzz():
    try:
        
        num = int(input('Write your number here: '))
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FizzBuzz')
        elif num % 3 == 0:
            print(num, 'Fizz')
        elif num % 5 == 0:
            print(num, 'Buzz')
        else:
            print(num, 'Not Divisible By Eithier 3 and 5')
    except:
            print('Input a VALID Number')
    restart = input('Do you wanna enter another number?, Y or N: ').lower()
    if restart == 'y':
        FizzBuzz()
    else:
        print('Bye!')

    


# In[ ]:


main()

