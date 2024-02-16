randomlist = ['A','B','A','B','V','D','R','T','T','D','V','B','V']

frequency = {}

for item in randomlist:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
