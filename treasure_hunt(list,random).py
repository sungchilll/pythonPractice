import random
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("보물이 어디 있을까요? [답변 예시) 1번째 가로줄에 3번째 자리 = 13] : ")

x = random.randint(0, 2)
y = random.randint(0, 2)

map[x][y] = "🟥"

row = int(position[0])-1
line = int(position[1])-1


if map[row][line] == "🟥":
    print(f"정답입니다. \n{row1}\n{row2}\n{row3}")
else:
    print(f"틀렸습니다. 보물의 위치는 \n{row1}\n{row2}\n{row3}")