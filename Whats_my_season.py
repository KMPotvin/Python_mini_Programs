print("What month would you like to know the season for?")
input_month = input()
print("And what day specifically")
input_day = int(input())
month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



if input_month == month_list[0] and 0 < input_day <= 31:
        print('Winter')
elif input_month == month_list[1] and 0 < input_day <= 29:
        print('Winter')
elif input_month == month_list[2] and 0 < input_day <= 19:
        print('Winter')
elif input_month == month_list[2] and 19 < input_day <= 31:
        print('Spring')
elif input_month == month_list[3] and 0 < input_day <= 30:
        print('Spring')
elif input_month == month_list[4] and 0 < input_day <= 31:
        print('Spring')
elif input_month == month_list[5] and 0 < input_day <= 20:
        print('Spring')
elif input_month == month_list[5] and 20 < input_day <= 30:
        print('Summer')
elif input_month == month_list[6] and 0 < input_day <= 31:
        print('Summer')
elif input_month == month_list[7] and 0 < input_day <= 31:
        print('Summer')
elif input_month == month_list[8] and 0 < input_day <= 21:
        print('Summer')
elif input_month == month_list[8] and 21 < input_day <= 30:
        print('Autumn')
elif input_month == month_list[9] and 0 < input_day <= 31:
        print('Autumn')
elif input_month == month_list[10] and 0 < input_day <= 30:
        print('Autumn')
elif input_month == month_list[11] and 0 < input_day <= 20:
        print('Autumn')
else:
    print('Invalid')