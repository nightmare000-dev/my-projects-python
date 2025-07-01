import datetime as dt

getCurrentDay = dt.datetime.now()
currentYear = dt.datetime.now().year

winter = dt.datetime(currentYear, 12, 1)
spring = dt.datetime(currentYear+1, 3, 1)
summer = dt.datetime(currentYear+1, 6, 1)
autumn = dt.datetime(currentYear, 9, 1)

months = [
    '1. Winter',
    '2. Spring',
    '3. Summer',
    '4. Autumn'
]

for i in months: print(i)

try: 
    getMonth = int(input("\nEnter the number of month : "))
    
    if getMonth == 1:
        difference = winter - getCurrentDay
        days = difference.days
        seconds = difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Until winter left {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    elif getMonth == 2:
        difference = spring - getCurrentDay
        days = difference.days
        seconds = difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Until spring left {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    elif getMonth == 3:
        difference = summer - getCurrentDay
        days = difference.days
        seconds = difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Until summer left {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    elif getMonth == 4:
        difference = autumn - getCurrentDay
        days = difference.days
        seconds = difference.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        print(f"Until autumn left {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    else: print(f"The number {getMonth} is not in the list! Please try again.")

except: print("Your symbol(s) is/are not the number!\nPlease try again.")