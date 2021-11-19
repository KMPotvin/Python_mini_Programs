import datetime

first_name = input('What is your name? ')
age = int(input('How old are you? '))
x = datetime.datetime.now()
year = x.strftime("%Y")
birth_year = int(year) - age

print('Hello {name}! You were born in {birth}'.format(name=first_name, birth=birth_year))
