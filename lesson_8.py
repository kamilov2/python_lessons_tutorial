# a = ['apple','banana', 'orange', 'cherry', 'ananas', 'mango']
# target_item = 'orange'
# for i in a:
#     print(i)

    
# a = [1, -10, 50, 60, -1, 15, -2, -85]
# x = 0 
# for i in a:
#     if i > 0:
#         x += i
# print(x)
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
# d = 0
# for i in x:
#     if i % 2 == 0:
#         d += 1
# print(d)
    
my_list = [1, 2, 3].append(4)
my_list.append(4)
print(my_list)  # Natija: [1, 2, 3, 4]

# clear() metodini ishlatish misoli
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Natija: []

# copy() metodini ishlatish misoli
my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Natija: [1, 2, 3]

# count() metodini ishlatish misoli
my_list = [1, 2, 2, 3, 3, 3]
count_3 = my_list.count(3)
print(count_3)  # Natija: 3

# extend() metodini ishlatish misoli
my_list = [1, 2, 3]
another_list = [4, 5]
my_list.extend(another_list)
print(my_list)  # Natija: [1, 2, 3, 4, 5]

# index() metodini ishlatish misoli
my_list = [1, 2, 3, 4, 5]
index_3 = my_list.index(3)
print(index_3)  # Natija: 2

# insert() metodini ishlatish misoli
my_list = [1, 2, 3]
my_list.insert(1, 1.5)
print(my_list)  # Natija: [1, 1.5, 2, 3]

# pop() metodini ishlatish misoli
my_list = [1, 2, 3]
popped_element = my_list.pop(0)
print(my_list)  

# remove() metodini ishlatish misoli
my_list = [1, 2, 3]
my_list.remove(2)
print(my_list)  # Natija: [1, 3]

# reverse() metodini ishlatish misoli
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Natija: [3, 2, 1]

# sort() metodini ishlatish misoli
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Natija: [1, 2, 3]



# s = [15, 56, 65, -58, 68, -57, -10]
# x = []
# y = []
# for i in s:
#     if i > 0:
#         x.append(i)
#     else:
#         y.append(i)
# print(x)
# print(y)



