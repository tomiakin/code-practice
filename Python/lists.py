

nums = [2, 4, 6]
accum = []
for w in nums:
    x = w**2
    accum.append(x)
print(accum)


seat_counts = [5, 7, 9, 11]
total_seat_counts = sum(seat_counts)
print(total_seat_counts)

nums = [4, 5, 2, 93, 3, 5]
s = 0
for n in nums:
    s = s + n
print(s)

s = "This is my all of my done"
vow = ['a', 'e', 'i', 'o', 'u']
recorded_vowels = []
for vowel in s:
    if vowel in vow:
        recorded_vowels.append(vowel)
print(recorded_vowels)

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print(a)

b = "My, what a lovely day"
x = b.split(',')
print(x[1])
z = "".join(x)
print(z)
y = z.split()
a = "".join(y)
print(a)


