def divide(x):
    return x/2

def sum(y):
    return divide(y) + 6


gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}

gold_items = gold.items()

num_medals = []

for item in gold_items:
    num_medals.append(item[1])

print(num_medals)

str1 = "peter piper picked a peck of pickled peppers"




freq = {}

for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] += 1

sally = "sally sells sea shells by the sea shore"

characters = {}

for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1
    
print(characters)
keys = list(characters.keys())

best_char = keys[0] # most freq character

for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print(best_char)
