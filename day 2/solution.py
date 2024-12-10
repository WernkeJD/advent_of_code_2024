

with open("input.txt", "r") as file:
    lines = file.readlines()

array_of_lines = []

for line in lines:
    temp = []
    split_line = line.split()
    for num in split_line:
        num_int = int(num)
        temp.append(num_int)

    array_of_lines.append(temp)


def calculate_increasing_direction_adherence(line):

    error_index = None

    for i in range(len(line) - 1):

        if line[i] < line[i + 1]:
            continue
        else:
            error_index = i
            return False, error_index
        
    return True, error_index

def calculate_decreasing_dircetion_adherence(line):

    error_index = None

    for i in range(len(line) - 1):
        if line[i] > line[i + 1]:
            continue
        else:
            error_index = i
            return False, error_index
        
    return True, error_index

def ensure_step_size_adherence(line, list_of_step_sizes):

    error_index = None

    for i in range(len(line) - 1):
        if abs(line[i] - line[i+1]) not in list_of_step_sizes:
            error_index = i
            return False, error_index
    
    return True, error_index

count = 0

for line in array_of_lines:
    #checks used for part one
    if calculate_increasing_direction_adherence(line)[0] == True and ensure_step_size_adherence(line, [1, 2, 3])[0] == True:
        count += 1
    elif calculate_decreasing_dircetion_adherence(line)[0] == True and ensure_step_size_adherence(line, [1, 2, 3])[0] ==True:
        count += 1

    #checks used for part two
    elif calculate_increasing_direction_adherence(line)[0] == False:
        _, error_index = calculate_increasing_direction_adherence(line)
        copy = line.copy()
        copy.pop(error_index)
        if calculate_increasing_direction_adherence(copy)[0] == True and ensure_step_size_adherence(copy, [1, 2, 3])[0] == True:
            count += 1
    elif calculate_decreasing_dircetion_adherence(line)[0] == False:
        _, error_index = calculate_decreasing_dircetion_adherence(line)
        line.pop(error_index)
        if calculate_decreasing_dircetion_adherence(line)[0] == True and ensure_step_size_adherence(line, [1, 2, 3])[0] ==True:
            count += 1
    elif ensure_step_size_adherence(line, [1,2,3])[0] == False:
        _, error_index = ensure_step_size_adherence(line, [1,2,3])
        line.pop(error_index)
        if calculate_increasing_direction_adherence(line)[0] == True and ensure_step_size_adherence(line, [1, 2, 3])[0] == True:
            count += 1
        elif calculate_decreasing_dircetion_adherence(line)[0] == True and ensure_step_size_adherence(line, [1, 2, 3])[0] ==True:
            count += 1
        
    else:
        # print(line)
        pass

print(count)