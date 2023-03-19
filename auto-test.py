import random

def monty_hall_test(num_trials):
    stay_wins = 0  # 선택을 유지했을 때의 성공 횟수
    switch_wins = 0  # 선택을 변경했을 때의 성공 횟수

    for i in range(num_trials):
        doors = [0, 0, 1]  # 문 리스트, 0은 염소, 1은 자동차
        random.shuffle(doors)  # 문 순서를 무작위로 섞음

        # 무작위로 하나의 문을 선택함
        first_choice = random.choice(doors)

        # 염소가 있는 문 하나를 공개하기
        if first_choice == 0:
            opened_door = random.choice([i for i in range(len(doors)) if doors[i] == 0 and i != first_choice])
        else:
            opened_door = doors.index(0)

        # 선택을 유지했을 때
        stay_choice = first_choice
        if doors[stay_choice] == 1:
            stay_wins += 1

        # 선택을 변경했을 때
        switch_choice = [i for i in range(len(doors)) if i != first_choice and i != opened_door][0]
        if doors[switch_choice] == 1:
            switch_wins += 1

        # 테스트 진행상황 출력하기
        if i % 1 == 0 and i > 0:
            stay_percent = stay_wins / i * 100
            switch_percent = switch_wins / i * 100
            print(f"\n{i}번 시도 중...")
            print(f"선택을 유지했을 때의 성공률: {stay_percent:.2f}%")
            print(f"선택을 변경했을 때의 성공률: {switch_percent:.2f}%")
            
    # 최종 결과 출력하기
    stay_percent = stay_wins / num_trials * 100
    switch_percent = switch_wins / num_trials * 100
    print(f"\n최종적으로 {num_trials}번 시도한 결과는:")
    print(f"선택을 유지했을 때의 성공률: {stay_percent:.2f}%")
    print(f"선택을 변경했을 때의 성공률: {switch_percent:.2f}%")
    return stay_percent, switch_percent


# 테스트 실행
num_trials = int(input("시도 횟수: "))
monty_hall_test(num_trials)