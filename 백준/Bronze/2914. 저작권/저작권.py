from sys import stdin

input = stdin.readline

song_num, song_avg = map(int, input().rstrip().split(" "))

print(song_num*(song_avg-1)+1)
