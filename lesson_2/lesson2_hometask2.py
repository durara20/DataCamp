## Stage 0 - setting pairs
def create_pairs():
    arr_2d = []

    i = 2
    j = 2
    for row in range(9_604):
        internal_arr = []

        for col in range(2):
            if col == 0:
                internal_arr.append(i)
            else:
                internal_arr.append(j)
                j += 1

        arr_2d.append(internal_arr)
    
        if j == 100:
            i += 1
            j = 2

    return arr_2d
        
pairs = create_pairs()

## Stage 1 - Prod: I don't know the numbers
def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

check = False
count = 0
while count in range(len(pairs)):
    internal_arr = pairs[count]

    if is_prime(internal_arr[0]) == True and is_prime(internal_arr[1]) == True:
        check = True    

    elif is_prime(internal_arr[0]) == True and internal_arr[0] > 50 or is_prime(internal_arr[1]) == True and internal_arr[1] > 50:
        check = True 

    if check == True:
        pairs.pop(count)
        count -= 1

    check = False
    count += 1

## Stage 2 - Sum: I know it
check = False
count = 0
while count in range(len(pairs)):
    internal_arr = pairs[count]

    if (internal_arr[0] + internal_arr[1]) % 2 == 0:
        check = True

    elif internal_arr[0] + internal_arr[1] > 52:
        check = True

    elif is_prime((internal_arr[0] + internal_arr[1]) - 2) == True:
        check = True

    if check == True:
        pairs.pop(count)
        count -= 1

    check = False
    count += 1

## Stage 3 - Prod: then I know the numbers;
##           Sum: then I know the numbers too.
def setSum(sum):
    count = 0    
    while count in range(len(pairs)):
        internal_arr = pairs[count]  

        if internal_arr[0] + internal_arr[1] > sum:
            sum = internal_arr[0] + internal_arr[1]
            break

        count += 1

    return sum

check = False
checkPlus = False
count = 0
checkCount = 0
Sum = 0

while check == False:
    sum = setSum(Sum)
    Sum = sum    
    if sum > 50:
        checkPlus = True

    while count in range(len(pairs)):
        internal_arr = pairs[count]    

        if internal_arr[0] + internal_arr[1] == sum:
            if internal_arr[0] == pow(2, 2) and is_prime(internal_arr[1]) == True or internal_arr[0] == pow(2, 3) and is_prime(internal_arr[1]) == True or internal_arr[0] == pow(2, 4) and is_prime(internal_arr[1]) == True or internal_arr[0] == pow(2, 5) and is_prime(internal_arr[1]) == True:
                checkCount += 1                

            elif internal_arr[1] == pow(2, 2) and is_prime(internal_arr[0]) == True or internal_arr[1] == pow(2, 3) and is_prime(internal_arr[0]) == True or internal_arr[1] == pow(2, 4) and is_prime(internal_arr[0]) == True or internal_arr[1] == pow(2, 5) and is_prime(internal_arr[0]) == True:
                checkCount += 1                
  
        count += 1

    if checkCount > 2:
        checkCount = 0
        count = 0
        while count in range(len(pairs)):
            internal_arr = pairs[count]

            if internal_arr[0] + internal_arr[1] == sum:
                pairs.pop(count)
                count -= 1

            count += 1
        count = 0
    else:
        checkCount = 0
        count = 0
        if checkPlus == True:
            check = True    

##
# 29 = 25 + 4
# 25 * 4 = 100 = 20 * 5 -> X
# 41 = 16 + 25
# 16 * 25 = 400 = 80 * 5 -> X
##

while count in range(len(pairs)):
    internal_arr = pairs[count]

    if internal_arr[0] + internal_arr[1] == 29 or internal_arr[0] + internal_arr[1] == 41:
        pairs.pop(count)
        count -= 1

    count += 1

##
# 17 = 2 + 15, 2 * 15 = 5 * 6 (sum is 11) — bad prod
# 17 = 3 + 14, 3 * 14 = 21 * 2 (sum is 23) — bad prod
# 17 = 4 + 13 — good
# 17 = 5 + 12, 5 * 12 = 20 * 3 (sum is 23) — bad prod
# 17 = 6 + 11, 6 * 11 = 33 * 2 (sum is 35) — bad prod
# 17 = 7 + 10, 7 * 10 = 35 * 2 (sum is 37) — bad prod
# 17 = 8 + 9, 8 * 9 = 24 * 3 (sum is 27) — bad prod
##

count = 0
while count in range(len(pairs)):
    internal_arr = pairs[count]

    if internal_arr[0] == 4 or internal_arr[0] == 13:
        check = True
    else:
        pairs.pop(count)
        count -= 1

    count += 1

print('The result of the program is ' + str(pairs))