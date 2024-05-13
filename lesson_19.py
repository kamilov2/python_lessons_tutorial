# input_str = input("Son ni kiriting: ")
# if len(input_str) == 5:
#     digits = [int(digit) for digit in input_str]
#     print(digits.reverse())
# else:
#     print("5 honali son kiriting !")

print("""
Amalardan birini tanlang:  
0 - ' / '
1 - ' * ' 
2 - ' - '
3 - ' + '
""")
def long_time(num1, element, num2):
    if element == 0:
        return num1 / num2
    elif element == 1:
        return num1 * num2
    elif element == 2:
        return num1 - num2
    else:
        return num1 + num2
print(long_time(int(input("1 sonni kiriting: ")), int(input("Matematik amalni kiriting: ")) , int(input("2 son ni kiriting: "))))
    



     



