from sys import stdin

# a시간당 얻는 피로도 b진행도  c시간당 줄어드는 피로도 m최대 피로도
a,b,c,m = map(int, stdin.readline().split(" "))

time = 24
farigue = 0
work = 0

for _ in range(time):
    if farigue + a <= m:
        farigue += a
        work += b
    else:
        farigue = max(0, farigue - c)

print(work)