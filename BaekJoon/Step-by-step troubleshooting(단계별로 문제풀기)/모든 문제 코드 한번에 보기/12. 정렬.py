# -*- coding: utf-8 -*-
"""백준 단계별로문제풀기 정렬 단계

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x1eBrB4vTjekU0_wvYmhrJ4eHnE1nfEN
"""

#2750번 수 정렬하기
n = int(input())
arr = []

for i in range(n) : 
  arr.append(int(input()))

arr.sort()

for i in range(n) :
  print(arr[i])

#2751번 수 정렬하기2
import sys
n = int(sys.stdin.readline())
arr = []

for i in range(n) : 
  arr.append(int(sys.stdin.readline()))

arr.sort()
for i in range(n) :
  print(arr[i])

#10989번 수 정렬하기3
import sys
input = sys.stdin.readline
n = int(input())
count = [0]*10001

for i in range(n) : 
  count[int(input())] += 1

for i in range(10001) : 
  for j in range(count[i]) : 
    print(i)

#2108번 통계학
import sys
input = sys.stdin.readline
n = int(input())
arr = []
count = [0]*8001 #음수도 나오기 때문에 음수의 크기를 고려하여 배열 크기 선정
count_max = 0

for i in range(n) : 
  temp = int(input())
  arr.append(temp)
  count[temp+4000] += 1

arr.sort()
print(round(sum(arr)/n))
print(arr[n//2])

for i in range(8001) : #최빈값이 여러개 나오는 경우를 확인하기 위함
  if count[i] == max(count) : 
    count_max += 1

if count_max == 1 : #최빈값이 한 개인 경우
  print(count.index(max(count))-4000)
else :              #최빈값이 여러개인 경우
  temp = 0
  for i in range(8001) : 
    if count[i] == max(count) and temp == 1 :
      print(i-4000)
      break
    if count[i] == max(count) : #최빈값 중 두번째로 큰 수를 출력하기 위함
      temp += 1

print((max(arr)-min(arr)))

#1472번 소트인사이드
n = int(input())

arr = []
while n :
  arr.append(n%10)
  n = n//10

arr.sort(reverse=True) #내림차순으로 정렬

for i in range(len(arr)) : 
  print(arr[i],end='')

#11650번 좌표 정렬하기
n = int(input())

xy = [[0]*2 for i in range(n)]

for i in range(n) :
  temp_x, temp_y = input().split()
  xy[i][0] = int(temp_x)
  xy[i][1] = int(temp_y)

result = sorted(xy, key = lambda x : (x[0],x[1]))  

for i in range(n) : 
  print("%d %d"%(result[i][0],result[i][1]))

#11651번 좌표 정렬하기2
n = int(input())

xy = [[0]*2 for i in range(n)]

for i in range(n) :
  temp_x, temp_y = input().split()
  xy[i][0] = int(temp_x)
  xy[i][1] = int(temp_y)

result = sorted(xy, key = lambda x : (x[1],x[0]))  

for i in range(n) : 
  print("%d %d"%(result[i][0],result[i][1]))

#1181번 단어 정렬
n = int(input())

words = []
for i in range(n) : 
  words.append(input())

words.sort()
words.sort(key=lambda x:len(x))
result = []

for i in range(n) : 
  if i == 0 :
    result.append(words[i])
  elif result[len(result)-1] == words[i] : 
    continue
  else : 
    result.append(words[i])

for i in range(len(result)) : 
  print(result[i])

#10814번 나이순정렬
n = int(input())

user = [[0]*3 for i in range(n)]

for i in range(n) : 
  age,name = input().split()
  age = int(age)
  user[i][0] = age
  user[i][1] = name
  user[i][2] = i

user.sort(key=lambda x:(x[0],x[2]))

for i in range(n) : 
  print(user[i][0], end = ' ')
  print(user[i][1])

21
