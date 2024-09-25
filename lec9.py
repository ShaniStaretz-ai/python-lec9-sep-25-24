# # ex1:
# l1 = [];
# count = 0
# while True:
#     name: str = input("enter name:")
#     if name.upper() == 'exit'.upper():
#         break;
#     if not name in l1:
#         l1.append(name)
#     print(l1)

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")


