"""
Author: Opoola Paul
Date: June 2019
program function: Prints Calendar of inputed year
---------------------------------------------------------------------------------------
TYPE IN THE YEAR (as 2019, 2002, 1893 etc) AND IT PRINTS THE CALENDAR FOR THE WHOLE YEAR
----------------------------------------------------------------------------------------
"""
import calendar


def CreateCalendar(year):
    for month in range(1,13):
        print(calendar.month(year,month))
checking = True
while checking:
    try:
        year_input = int(input('Which Calender Year do you wish to see: '))
        print('This is the Calendar for year {}'.format(year_input))
        CreateCalendar(year_input)
        year_input2 =str(input('Do you want to see the calendar for another year ?, Y or N ?')).lower()
        if year_input2[0] == 'y':
            checking = True
        else:
            print('Thanks!!!')
            checking = False

    except:
        print('Enter a Valid Year input, eg "2019"')
