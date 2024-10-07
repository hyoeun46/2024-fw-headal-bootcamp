try:
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)
    else:
        print("좌표가 원점에 있습니다.")

except ValueError:
    print("정수를 입력하세요.")