numbers: list[int] = [];
count_numbers: list[int] = []
SENTINEL: int = -999;

for _ in range(10):
    count_numbers.append(0)
while True:
    number: int = int(input("enter temperature:"))
    if number == SENTINEL:
        break;
    if number > 10 or number < 0:
        continue;
    count_numbers[number - 1] += 1
    str_results = ''
    for i in range(len(count_numbers)):

        if count_numbers[i]:
            str_results += f'[{i + 1}]:{count_numbers[i]} '
    else:
        print('Statistics:' + str_results)
