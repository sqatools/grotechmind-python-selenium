
def find_hcf(num1, num2):
    if num1> num2:
        small = num2
    else:
        small = num1

    for i in range(1, small+1):
        if num1%i == 0 and num2%i == 0:
            hcf = i
        print("hfc :", hcf)


#find_hcf(24, 54)
#find_hcf(15, 45)


def find_lcf(num1, num2):
    if num1> num2:
        bigger = num1
    else:
        bigger = num2

    for i in range(bigger, 1, -1):
        if num1%i == 0 and num2%i == 0:
            lcf = i
            print("lcf :", lcf)




find_lcf(24, 54)

