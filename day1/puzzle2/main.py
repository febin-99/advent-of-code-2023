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
        num = int(num)
    
    first_num_index = line.find(str(num//10))
    
    if first_num_index == -1:
        first_num_index = len(line)

    found = False

    for i in range(first_num_index):
        for key in number_dict.keys():

            if line[:i + 1].__contains__(key):
                num = number_dict[key] * 10 + num % 10
                found = True
                break
        if found:
            break
    last_num_index = line.rfind(str(num % 10))
    if last_num_index == -1:
        last_num_index = 0
    found = False
    
    for i in range(0, len(line) - last_num_index):
        for key in number_dict.keys():
            if line[:-i-1:-1].__contains__(key[::-1]):
                num -= num % 10
                num += number_dict[key]
                found = True
                break
        if found:
            break
    print(num)
    sum += num
    
print(int(sum))