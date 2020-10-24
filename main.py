import sys

#f = sys.stdin
f = open('data.txt', 'r')

N = int(f.readline().rstrip())

temp = N
result = -1
#안나눠질 때 -1이므로 기본 -1로 초기화
if temp % 5 == 0:
    result = temp // 5

for i in range(0, N, 3):#0~N 3씩 늘어남
  temp = N - i
  if temp % 5 == 0: #5kg으로 최대한 나누기
    result = (temp//5 + i//3)
    break
if result == -1:
  if N % 3 == 0:
    result = N // 3

print (result)