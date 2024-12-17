#test data
with open("test_data.txt", "r") as file:
    file_lines = file.readlines()

test_array = []

for line in file_lines:
    for character in line:
        test_array.append(character)

##############################



with open("input.txt", "r") as file:
    lines = file.readlines()


character_array = []

for line in lines:
    for character in line:
        character_array.append(character)


print(character_array[:3])
stringed_subarray = ''.join(character_array[:3])
print(stringed_subarray)

"""
arr = array of input data
k = size of windows
n = len of array
"""
def find_muls(arr, k):
    n = len(arr)

    running_total = 0

    initial_window = arr[:k]

    stringed_window = ''.join(initial_window)

    initial_mul_numbers = []

    if stringed_window == "mul(":
        for character in arr[k:]:
            if character.isdigit():
                initial_mul_numbers.append(character)
            elif character == ',':
                initial_mul_numbers.append(character)
            else:
                if character == ')':
                    break
    
        split_init_nums = ''.join(initial_mul_numbers).split(',')

        running_total += (int(split_init_nums[0]) * int(split_init_nums[1]))

    temp_array = []

    for i in range(n - k):
        start_index = i+1
        end_index = i+1+k
        window = arr[start_index: end_index]

        stringed_window = ''.join(window)

        if stringed_window == "mul(":
            for character in arr[end_index:]:
                if character.isdigit():
                    temp_array.append(character)
                elif character == ",":
                    temp_array.append(character)
                else:
                    if character == ")":
                        break
                    elif character == " ":
                        break
       
            split_nums = ''.join(temp_array).split(',')
            if len(split_nums) == 2:
                print(split_nums)
                print(split_nums[0])
                print(split_nums[1])
                running_total += (int(split_nums[0]) * int(split_nums[1]))
                temp_array = []
            else:
                temp_array = []




    return running_total


# print(find_muls(character_array, 4))

print(find_muls(test_array, 4))




