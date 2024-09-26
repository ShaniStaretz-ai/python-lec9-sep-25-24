temperatures: list[float] = [];
SENTINEL: int = -999;
while True:
    temp: float = float(input("enter temperature:"))
    if temp == SENTINEL:
        break;
    if temp > 50 or temp < -50:
        continue;
    temperatures.append(temp);

temperatures.extend([-20, 39.1, 18.5])
newList: list[int] = [4, 5, 6] + [1, 2, 3];  # creates a new list with both lists
[4, 5, 6].extend([1, 2, 3])  # changes the list [4,5,6] itself
print("max:", max(temperatures));
print("min:", min(temperatures));
print(f"is 18.5 in list temperatures:{18.5 in temperatures}");
count_temp_minus_20: int = temperatures.count(-20);
print(f"avg temperatures:{sum(temperatures) / len(temperatures):.2f}");
print("temperature:", end=' ');
for temperature in temperatures:
    print(temperature, end=' ');
print()
if 39.1 in temperatures:
    index_39_1: int = temperatures.index(39.1);
del temperatures[0];
del temperatures[::2];
if 18.5 in temperatures:  # remove function will give an error
    temperatures.remove(18.5);
temp_last: float = temperatures.pop()
new_temperatures: list[float] = temperatures.copy();
new_temperatures.sort();
new_temperatures2: list[float] = temperatures.copy();
new_temperatures2.sort(reverse=True);
