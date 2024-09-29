SENTINEL: int = -999;
numbers: list[int] = []
uniques: list[int] = []
counts: list[int] = []
while True:
    number: int = int(input("enter temperature:"))
    if number == SENTINEL:
        break;
    if number > 10 or number < 0:
        continue;
    numbers.append(number)

    for i in range(11):
        counter = numbers.count(i)
        if counter:
            print(f"[{i}]:{counter}", end=' ')
    print()
