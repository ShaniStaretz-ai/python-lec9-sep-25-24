count_numbers: list[int] = []
SENTINEL: int = -999;

for _ in range(100):
    count_numbers.append(0)
while True:
    number: int = int(input("enter temperature:"))
    if number == SENTINEL:
        break;
    if number > 100 or number < 0:
        continue;
    count_numbers[number - 1] += 1

str_results:str = ''
for i in range(len(count_numbers)):
    str_results += f'[{i + 1}]:{count_numbers[i]} '
print('Statistics:' + str_results)
