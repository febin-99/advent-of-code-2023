calibration_document = open('dummy_input.txt')

# calibration_document = open('input.txt')

number_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

sum = 0
for line in calibration_document:
    for i in range(len(line)):
        for key in number_dict.keys():
            if line[0:i].__contains__(key):
                line = line.replace(key, str(number_dict[key]))     
    # print(line)
    num = 0
    char_taken = 0
    for char in line:
        try:
            if int(char):
                if char_taken == 0:
                    num += int(char) * 10
                elif char_taken > 1:
                    num -= num % 10
                    num += int(char)
                else:
                    num += int(char)
                char_taken += 1
        except:
            continue
    if char_taken == 1:
        num *= 11/10
    print(num)
    sum += int(num)

print(int(sum))