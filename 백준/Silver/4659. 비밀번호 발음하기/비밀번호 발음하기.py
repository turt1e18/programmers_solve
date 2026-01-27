from sys import stdin

input = stdin.readline

vowel = ['a','e','i','o','u']

while True:
    input_string = list(input().rstrip())

    is_accept = False

    vowel_duplication = 0
    conson_duplication = 0
    past_alpha = ""

    if "end" == "".join(input_string):
        break

    if any(char in input_string for char in vowel) != True:
        print("<"+"".join(input_string)+"> is not acceptable.")
        continue

    for i in input_string:
        

        if i in vowel:
            vowel_duplication += 1
            conson_duplication = 0
        else:
            conson_duplication += 1
            vowel_duplication = 0
        
        if (i + past_alpha not in ("ee","oo")) and i == past_alpha:
            is_accept = False
            break
        
        if vowel_duplication >= 3 or conson_duplication >= 3:
            is_accept = False
            break
        else:
            is_accept = True
        
        past_alpha = i

    if is_accept is False: print("<"+"".join(input_string)+"> is not acceptable.")
    else: print("<"+"".join(input_string)+"> is acceptable.")