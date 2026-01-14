from sys import stdin

input = stdin.readline

hour, min, sec = map(int, input().rsplit(" "))
timer = int(input().rstrip())

add_sec = int(timer % 60)
add_min = timer // 60
add_hour = 0

if add_min >= 60:
    add_hour = add_min // 60
    add_min = add_min - (60 * add_hour)

re_sec = add_sec + sec
re_min = add_min + min
re_hour = add_hour + hour

if re_sec >= 60 :   
    re_sec = re_sec - 60
    re_min = re_min + 1

if re_min >= 60 :   
    re_min = re_min - 60
    re_hour =  re_hour + 1

if re_hour >= 24:
    re_hour = re_hour % 24  

print(re_hour, re_min, re_sec)