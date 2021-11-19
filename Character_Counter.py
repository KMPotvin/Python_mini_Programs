print("What would you like to know the character count of (excluding: spaces, commas, and periods .")
user_text = input()
char_count = 0

for i in range(len(user_text)):
    if user_text[i] != ' ':
        if user_text[i] != ',':
            if user_text[i] != '.':
                char_count += 1
    else:
        char_count += 0

print(char_count)