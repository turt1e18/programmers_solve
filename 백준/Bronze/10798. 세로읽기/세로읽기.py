from sys import stdin

a = list(map(str,stdin.readline().rstrip()))
b = list(map(str,stdin.readline().rstrip()))
c = list(map(str,stdin.readline().rstrip()))
d = list(map(str,stdin.readline().rstrip()))
e = list(map(str,stdin.readline().rstrip()))
maxLen = max(len(a),len(b),len(c),len(d),len(e))

result = ""

# print( a,b,c,d,e)
for i in range(maxLen):
    if(i < len(a)):
        result = result + str(a[i])
    
    if(i < len(b)):
        result = result + str(b[i])
    
    if(i < len(c)):
        result = result + str(c[i])
    
    if(i < len(d)):
        result = result + str(d[i])
    
    if(i < len(e)):
        result = result + str(e[i])
    
print(result)