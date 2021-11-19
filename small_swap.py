def swap_values(user_val1, user_val2):
    t = user_val1
    user_val1 = user_val2
    user_val2 = t
    swap_values = user_val1, user_val2
    return swap_values

if __name__ == '__main__':
    print("What is the first value you to swap?")
    user_val1 = int(input())
    print("What is your second value?")
    user_val2 = int(input())
    print(*swap_values(user_val1, user_val2))