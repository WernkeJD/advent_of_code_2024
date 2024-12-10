import numpy as np

data = np.loadtxt("input.txt")

l_data = [row[0] for row in data]
r_data = [row[1] for row in data]

l_data.sort()
r_data.sort()

running_total = 0

for list in zip(l_data, r_data):
    running_total += int(abs(list[0] - list[1]))

freq = {}
similarity_score = 0

for i in l_data:
    if i in freq.keys():
        similarity_score += freq[i]
        continue
        
    count = 0

    for j in r_data:
        if i == j:
            count += 1
            
    freq.update({i: i * count})
    similarity_score += i * count

similarity_score = int(similarity_score)



print(running_total)
print(similarity_score)


