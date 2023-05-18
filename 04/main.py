#1
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(scores, cutline):
    answer = 0
    for score in scores:
        if score >= 60:
            answer += 1 
    return answer

scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)
print("solution 함수의 반환 값은", ret, "입니다.")

#2
def get_rank(scores, score):
    rank = 1
    for s in scores:
        if s == score:
            return rank
        rank += 1
    return 0

def sort(arr):
    arr.sort(reverse=True) # arr 정렬

def get_score(arr, n):
    return arr[n]

def solution(scores, n):
    score = scores(n)
    @@@
    answer = @@@
    return answer

scores = [20, 60, 98, 59]
n = 3
ret = solution(scores, n)
print("solution 함수의 반환 값은", ret, "입니다.")

scores = [80, 31, 17, 20, 60, 98, 59, 88, 75]
n = 1
ret = solution(scores, n)
print("solution 함수의 반환 값은", ret, "입니다.") # 7
  #3
def solution(num_apple, num_carrot, k):
    answer = 0
    
    if num_apple < num_carrot * 3:
        answer = num_apple // 3
    else:
        answer = num_carrot    

    num_apple -= answer * 3
    num_carrot -= answer

    i = 0
    while k - (num_apple + num_carrot + i) > 0:
        if i % 4 == 0:
            answer += 1
        i += 1
    return answer
    
num_apple1 = 5
num_carrot1 = 1
k1 = 2
ret1 = solution(num_apple1, num_carrot1, k1)
print("solution 함수의 반환 값은", ret1, "입니다.")

num_apple2 = 10
num_carrot2 = 5
k2 = 4
ret2 = solution(num_apple2, num_carrot2, k2)
print("solution 함수의 반환 값은", ret2, "입니다.") # 2

num_apple3 = 100
num_carrot3 = 100
k3 = 10
ret3 = solution(num_apple3, num_carrot3, k3)
print("solution 함수의 반환 값은", ret3, "입니다.") # 33
