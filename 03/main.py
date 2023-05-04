#1
def solution(speed, cars):
    answer = 0
    for x in cars:
        if x >= speed * 11 / 10 and x < speed * 12 / 10:
            answer += 3
        elif x >= speed *12 / 10 and x < speed * 13 / 10:
            answer += 5
        elif x >= speed * 13 / 10:
            answer += 7
    return answer

speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)
print("solution 함수의 반환 값은", ret, "입니다.")

speed = 120
cars = [110, 98, 125, 148, 120, 112, 89, 150, 170, 90, 135]
ret = solution(speed, cars)
print("solution 함수의 반환 값은", ret, "입니다.") # 20

#2
def solution(taekwondo, running, shooting):
    answer = 0
    if taekwondo >= 25:
        answer += 250
    else:
        answer += taekwondo * 8
    answer += 250 + (60 - running) * 5
    count = 0
    for s in shooting:
        answer += s
        if s == 10:
            count += 1
    if count >= 7:
        answer += 100
    return answer

taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)
print("solution 함수의 반환 값은", ret, "입니다.")

taekwondo = 10
running = 75
shooting = [9, 10, 8, 6, 3, 4, 7, 10, 7, 10]
ret = solution(taekwondo, running, shooting)
print("solution 함수의 반환 값은", ret, "입니다.") # 329

#3
def solution(korean, english):
    answer = 0
    math = 210 - korean - english
    if math > 100:
        answer = -1
    else:
        answer = math
    return answer

korean = 70
english = 60
ret = solution(korean, english)
print("solution 함수의 반환 값은", ret, "입니다.")

korean = 80
english = 30
ret = solution(korean, english)
print("solution 함수의 반환 값은", ret, "입니다.") # 100

korean = 10
english = 10
ret = solution(korean, english)
print("solution 함수의 반환 값은", ret, "입니다.") # -1


















