#1
def solution(point):
	if point >= 1000:
		answer = point - (point % 100)
	return answer

point = 2323
ret = solution(point)
print("solution 함수의 반환 값은", ret, "입니다.")

point = 12345
ret = solution(point)
print("solution 함수의 반환 값은", ret, "입니다.") # 12300

#2
def solution(calorie):
    answer = 0
    min_cal = 1000
    
    for cal in calorie:
        if cal > min_cal:
            answer += (cal - min_cal)
        else:
            min_cal = cal

    return answer

calorie = [713, 665, 873, 500, 751]
ret = solution(calorie)
print("solution 함수의 반환 값은", ret, "입니다.")

calorie = [713, 665, 873, 500, 751, 1000, 778]
ret = solution(calorie)
print("solution 함수의 반환 값은", ret, "입니다.") # 1237

#3
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
