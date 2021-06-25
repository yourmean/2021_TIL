#BOJ_1065

#한수여부 판단
def han(x):
    check=[]
    out=0
    n = list(x)
    for i in range(len(n)-1):
        check.append(int(n[i])-int(n[i+1]))
    if len(set(check)) == 1 or int(x)<100:
        out+=1
    return out

#1~N 사이의 한수 개수
cnt=0
for i in range(int(input())):
    cnt+= int(han(str(i+1)))
print(cnt)

# 1~99: 한수
#자릿수간 차이 저장 후 set -> len=1이면 한수 count
