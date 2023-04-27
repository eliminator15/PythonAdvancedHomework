
def solution(point):
	if point >= 1000:
		answer = point * 0.97
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
