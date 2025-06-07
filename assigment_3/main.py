# Початковий рівень
my_list = [1,2,3,4,5]

#1
print(sum(my_list))

#2
print(min(my_list))

#3
rev = my_list[::-1]
print(rev)

#4
for i in my_list:
    if i % 2 != 0:
        print(i)

#5
new_list = []
for i in my_list:
    multiply = i * 5
    new_list.append(multiply)
print(new_list)

# Легкий
#1
my_list2 = [-3,-2,5,6,8,10]
new_list2 = []
for i in my_list2:
    if i > 5:
        new_list2.append(i)
print(new_list2)

#2
sum_num = 0
len_num = 0
for i in my_list2:
    if i > 0:
        sum_num += i
        len_num += 1
print(sum_num/len_num)

#3
count = 0
filtered = []
for i in my_list2:
    if i < 5:
        count += 1
        filtered.append(i)
print(max(filtered)) # я тут не зрозуміла формулювання 3 пункту, що таке "Максимальна кількість":( тому я знайшла максимальне число
print(count) # і кількість чисел

#4
sum_n = 0
for i in my_list2:
    if i % 2 == 0:
        sum_n += i
print(sum_n)

#5
squares = []
for i in my_list2:
    squares.append(i**2)
print(squares)

#6
new_list2 = []
for i in my_list2:
    if i > 0:
        new_list2.append(i)
print(new_list2)

#7
my_list3 = ["apple", "banana", "ananas"]
prefix = 'ba'
filtered = []
for i in my_list3:
    if i.startswith(prefix):
        filtered.append(i)
print(filtered)

#8
sum_num = sum(my_list2[:5])
print(sum_num)

#9
list_words = ["pop", "rock", "bib", "hey"]
palindromes = []
for word in list_words:
    if word == word[::-1]:
        palindromes.append(word)
print(palindromes)

#10
divided = []
divisor = 5
for i in my_list2:
        divided.append(i % divisor == 0)
print(divided)

#Середній рівень

#1
list3 = [1,3,5,7,9,10]
filtered = []
for i in list3:
    if i % 2 == 0 and 1 % 3 !=0:
        filtered.append(i)
print(filtered)

#2
test_list1 = [[1,2], ["hello","bye"]]
test_list2 = []
for lists in test_list1:
    for item in lists:
        test_list2.append(item)
print(test_list2)

#3
text = ["I LovE ОП(probably)"]
uppers = []
for word in text:
    for letter in word:
        if letter.isupper():
            uppers.append(letter)
print(uppers)

#4
nums = [10,10,13,5,5,5,6,7,3,1,1,2]
nums.sort(reverse=True) # За спаданням
print(nums)

freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
nums.sort(key=lambda x: freq[x], reverse=True) #За частотою
print(nums)

#5
test_list1 = [1,2,3,4,5]
test_list2 = [1,4,5,6,7,9]
test_list3 = []

for i in test_list1:
    if i > 3:
        test_list3.append(i)
for i in test_list2:
    if i % 3 == 0:
        test_list3.append(i)
print(test_list3)

#6
my_marks = {"ОП": [1,2,3,4,5], "Мікра": [6,7,8,9,10]}
for key,value in my_marks.items():
    my_marks[key] = sum(value)
print(my_marks)

#7
nums = [1,2,3,2,5,7,2,4]
for i in range(len(nums)):
    if nums[i] == 2:
        nums[i] = "lol"
print(nums)

#8
words = ["hello", "world", "kse", "deadline"]
long_words = []
count = 0
for word in words:
    if len(word) > 3:
        count += 1
        long_words.append(word)
print(f"{count} words:{long_words} are longer than 3 :)")

#9
list1 = ["I", "want", ":("]
list2 = ["really", "sleep"]
list3 = []
while True:
    try:
        for i in range(len(list1)):
            list3.append(list1[i])
            list3.append(list2[i])
    except IndexError:
        break
print(list3)

#10
last_list = [1,3,4,5,6,7,8,9,10]
last_list2 = []
for i in last_list:
    if i > 4:
        last_list2.append(i * 5)
    else:
        last_list2.append(i) #тут якщо я правильно зрозуміла то ж числа, які менше все одно треба залишати у списку...
print(last_list2)

#ура кінець