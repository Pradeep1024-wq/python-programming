count = int(input("ENTER THE COUNT OF NUMBERS: "))
n = 0
sum = 0
for n in range(count):
    pn = int(input("ENTER AN INTEGER: "))
    sum = sum + n
avg = sum/count
print("THE AVERAGE IS: ", avg)
