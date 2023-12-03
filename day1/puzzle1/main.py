# calibration_document = open('dummy_input.txt')

calibration_document = open('input.txt')

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
    sum += num

print(int(sum))