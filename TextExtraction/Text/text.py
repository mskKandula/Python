# with open('SampleText.txt') as file:
#     lines = file.read().split(".")
#     for line in lines:
#         print(line)


with open('SampleText.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        print("\n")