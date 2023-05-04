# 이번 과제를 하면서 가장 중요했던 것
# 딕셔너리의 key or value에서 특정값을 출력할때는
# list 형태로 만들어서 인덱스를 사용하여 출력하기 !!!
# list 형태로 만들지 않고 출력하여서 모두 error가 발생하였다.
# 이거는 꼭 알아두고 가자!!

import time
import random

print("""

  ___          _                    _   _____                         _
 / _ \        (_)                  | | /  __ \                       (_)
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/

""")

print("~ 모여봐요 멋사의 숲 ~\n")

name = input("당신의 이름은? ")  # 이곳을 채우세요
island = input("섬 이름은? (ㅇㅇ섬으로 입력됩니다.) ")  # 이곳을 채우세요

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(0.8)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    print()

    # 0. 게임 종료
    if answer_action == "0":
        time.sleep(0.8)
        print("\n게임을 종료합니다...")
        action_boolean = 0

        # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        time.sleep(0.8)
        print("상점에 온 걸 환영해구리!")
        time.sleep(0.8)
        print("현재 상점에는 이런 물건들이 있어구리")
        print()
        i = 0
        for item in store:
            i += 1
            print(i, ".", item, " : ", store[item])
        print()
        time.sleep(0.8)
        num = int(input("어떤 물건을 구입하겠어구리? (숫자로 입력) "))
        print()
        # store.key의 값과 store.value의 값을 모두 리스트로 한번 변환해준뒤에 출력해줘야 한다!!! 여기서 고생함 !!!
        # 이거 때문에 이 밑에 싹 다 수정함!!!
        if (my_bell - list(store.values())[num-1] > 0):
            my_bell -= list(store.values())[num-1]
            print(list(store.keys())[0], "을(를) 구입하셨습니다!")
            print("남은 벨 :", my_bell)
            # my_pocket = list(store.keys())[num-1]로 작성했더니 글자가 하나씩 추가되어 1.강 2.아 3.지 ...로 출력됨
            # 하나의 이름으로 추가되기 위해서는 append함수 사용!!
            my_pocket.append(list(store.keys())[num-1])
        else:
            print("벨이 부족합니다!")

        """
        if(num == 1) :
            print("가습기를 구입하셨습니다!")
            my_bell -= 1400
        elif(num == 2):
            print("강아지 인형을 구입하셨습니다!")
            my_bell -= 2400
        elif(num == 3):
            print("강의실 책상을 구입하셨습니다!")
            my_bell -= 2500
        elif(num == 4):
            print("몬스테라를 구입하셨습니다.")
            my_bell -= 1700
        """

        # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        time.sleep(0.8)
        print("우리 마을에 있는 주민이야")
        time.sleep(0.8)
        print()
        i = 0
        for ani_name in animal:
            i += 1
            print(i, ".", ani_name)
        time.sleep(0.8)
        print()
        friend = int(input("어떤 주민을 찾아갈까? (숫자로 입력) "))

        """
        # 여기서 answer_animal_action = int(input((list(animal.keys())[friend-1], "에게 무엇을 할까?")))
        # 라고 작성하니까 괄호랑 작은 따옴표까지 모두 출력한다
        # 그래서 chat gpt한테 물어보니까 +를 사용하여 두개의 문자열을 연결하면 된다고 알려주었다.
        # chat gpt 개좋아 !!! 근데 사실 이유는 잘 모르겠음...
        answer_animal_action = int(
            input(list(animal.keys())[friend-1] + "에게 무엇을 할까? "))

        #근데 여기서 문제였던 거는 말걸기, 선물하기, 때리기를 딕셔너리나 리스트로 정의하지 않았다
        # 위의 경우를 실행하면 말걸기, 선물하기, 때리기가 출력되지 않는다.
        # 따라서 두번에 나눠서 아래와 같이 출력하게 하였다.
        """

        print()
        print(list(animal.keys())[friend-1] + "에게 무엇을 할까?")
        answer_animal_action = int(input("1. 말걸기 2. 선물하기 3. 때리기 "))

        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            time.sleep(0.8)
            print(list(animal.keys())[friend-1], ": 안녀엉~ ", name, "야~ 반가워어~")
            animal[list(animal.keys())[friend-1]] += 1
            print(list(animal.keys())[friend-1], "친밀도 +1")

            # 2-1. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            time.sleep(0.8)
            print()
            print("내 주머니엔 이렇게 있어")
            # my_pocket 출력하기
            i = 0
            for things in my_pocket:
                i += 1
                print(i, ".", things)
            print()
            time.sleep(0.8)
            gift = int(input(("어떤 것을 선물할까? (숫자로 입력) ")))
            # 여기가 제일 헷갈렸다.
            gift_animal = my_pocket[gift - 1]
            # print(list(animal.keys()[friend-1]), "에게",list(my_pocket.keys()[gift-1]), "을(를) 선물했다!")
            # 로 작성했다가 뭔가 이상했다...!
            print(list(animal.keys())[friend-1],
                  "에게", gift_animal, "을(를) 선물하였다.")
            my_pocket.remove(gift_animal)
            animal[list(animal.keys())[friend-1]] += 5
            print(list(animal.keys())[friend-1], '친밀도 +5')

            # 2-3. 떄리기를 선택한 경우
        elif answer_animal_action == 3:
            time.sleep(0.8)
            print(list(animal.keys())[friend-1], ": 응...?! 아야! 왜 그러는거야!")
            time.sleep(0.8)
            print(list(animal.keys())[friend-1], "을(를) 때렸다!")
            time.sleep(0.8)
            animal[list(animal.keys())[friend-1]] -= 1
            print(list(animal.keys())[friend-1], "친밀도 -1")

            # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        time.sleep(0.8)
        print("나무를 흔듭니다.")
        print("응...?")
        result = random.choice(['100벨', '사과', '벌'])
        # 100벨이 떨어질경우
        if result == "100벨":
            print("100벨이 떨어졌습니다!")
            my_bell += 100
            # 사과가 떨어질경우
        elif result == "사과":
            print("사과가 떨어졌습니다!")

            # 벌이 나타날경우
        elif result == "벌":
            print("벌이 나타났습니다!")
            print("아야... 벌에게 물렸어")

            # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        time.sleep(0.8)
        print("내 정보")
        # 이름 출력
        print("- 이름 :", name)

        # 남은 벨 출력
        time.sleep(0.5)
        print("- 남은 벨 :", my_bell)

        # 주머니 출력
        time.sleep(0.5)
        pocket = bool(my_pocket)
        if (pocket == False):
            print("- 내 주머니 : 비었음")
        else:
            print("- 내 주머니 :", *my_pocket)

        # 주민 친밀도 출력
        print("- 주민과 친밀도 :")
        i = 0
        for key, value in animal.items():
            i += 1
            print("   ", i, ".", key, " : ", value)

        # 잘못된 입력을 했을경우
    else:
        print("제대로 입력해주구리!")
