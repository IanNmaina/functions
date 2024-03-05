def divisibility_test(num):
    if num %10==0:
        return True
    else:
        return False
num=int(input("Enter a number"))
result = divisibility_test(num)
print("Is num divisible by 10",result,num)
