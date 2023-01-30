# lower=int(input("Please enter the lower Range value"))
# upper=int(input("Please enter the upper Range value"))
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(num, "is  not a prime number")
#                 break 
#         else:
#             print(f"The prime numbers in the range are",num)
start=int(input("please enter the start range value"))
end=int(input("please enter the end range value"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(f"The prime numbers are",i)
