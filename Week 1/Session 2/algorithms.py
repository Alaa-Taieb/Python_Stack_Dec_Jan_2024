

# To calculate the factorial of a number
# 3! = 3 * 2 * 1 = 6
# 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2 * 1
def factorial(number):
    # number = number * (1)
    # number = number * (2)
    # number = number * (3)
    # number = number * (4)
    for i in range(1,number):
        number = number * i
    return number
    
print(factorial(9))
# Given a list return the biggest number in that list
# [5,10,9,12] => 12
# Assume 5 is the biggest number | max = 5
# Compare max and 10 | 10 > max | max = 10

def max_number(list):
    if list == []:
        print("this is an empty list.")
    else:
        max = list[0]
        if len(list) != 1:
            for i in range(1,len(list)):
                if max < list[i]:
                    max = list[i]
        return max
    

    
max_number = max_number([10])
print(max_number)

def lazy_max(list):
    return max(list)

print(lazy_max([5,10,9,12]))

# A recursive function is a function that instead of using loops it call it self.