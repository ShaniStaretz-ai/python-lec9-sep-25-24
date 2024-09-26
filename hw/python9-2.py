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
    count = numbers.count(number)
    for x in numbers:
        if x not in uniques:
            uniques.append(x)
            uniques.sort()
        counts.insert(uniques.index(x), count)
    for i in range(len(uniques)):
        print(f"[{uniques[i]}]:{counts[i]}", end=' ')
    print()
