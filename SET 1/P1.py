lower_num=int(input("Enter the lowest range: "))
upper_num=int(input("Enter the upper range: "))
print("The Prime numbers in the range are: ")
for num in range(lower_num , upper_num + 1):
    if num > 1:
        for j in range(2,num):
            if (num%j) == 0:
                break
        else:
            print(num)


