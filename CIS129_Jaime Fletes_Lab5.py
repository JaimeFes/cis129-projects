# Module 5 Lab-5
# Jaime Fletes
# 2/26/2024
# calculates total payout by amount of bottles returned

# Lab 5 The Bottle Return Program


NBR_OF_DAYS = 7
total_bottles = 0
today_bottles = 0
counter = 1
keep_Going = 'y'

while keep_Going == 'y':
    print(f'Enter number of bottles returned for day "{counter}": ')
    today_bottles = int(input())
    total_bottles = total_bottles + today_bottles 
    counter += 1
    
    if counter > NBR_OF_DAYS:
        PAY_OUT_PER_BOTTLE = 0.10
        totalPayout = total_bottles * PAY_OUT_PER_BOTTLE
            
        print(f"The total amount of bottles returned: {total_bottles}")
        print(f"The total amount paid out: {totalPayout:.1f}")
        
        keep_Going = input('Do you want to enter another week’s worth of data? (y or n): ')
        if keep_Going == 'y':
            counter = 1
            total_bottles = 0
