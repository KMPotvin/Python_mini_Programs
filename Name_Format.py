print("What is your full name?")
name = input()
break_name = name.split(' ')
last_name= break_name [-1]
first_inital = break_name[0][0]


if len(break_name) >= 3:
   middle_inital = break_name[1][0]
   print(last_name+', '+first_inital+'.'+middle_inital+'.')
else:
    print(last_name+', '+first_inital+'.')