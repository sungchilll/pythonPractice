import random

user = int(input("가위 = 0, 바위 = 1, 보 = 2 : "))

computer = random.randint(0, 2)
if user == 0:
    user_answer = "가위"
elif user == 1:
    user_answer = "바위"
elif user == 2:
    user_answer = "보"

if computer == 0:
    computer_answer = "가위"
elif computer == 1:
    computer_answer = "바위"
elif computer == 2:
    computer_answer = "보"

if user >=3 or user < 0:
    print("잘못입력하셨습니다.")
else:
    print(f"당신은 {user_answer}, 컴퓨터는 {computer_answer}")

if user == 0 and computer == 0:
    print("비겼습니다.")
elif user == 0 and computer == 1:
    print("당신이 졌습니다.")
elif user == 0 and computer == 2:
    print("당신이 이겼습니다.")

if user == 1 and computer == 1:
    print("비겼습니다.")
elif user == 1 and computer == 2:
    print("당신이 졌습니다.")
elif user == 1 and computer == 0:
    print("당신이 이겼습니다.")

if user == 2 and computer == 2:
    print("비겼습니다.")
elif user == 2 and computer == 0:
    print("당신이 졌습니다.")
elif user == 2 and computer == 1:
    print("당신이 이겼습니다.")