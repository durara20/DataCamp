d=[]
def prime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
         if (num % i) == 0:
            return False
            break
         else:
            return True
    else:
       return False
for i in range(2,100):
    for j in range(2,100):
        l=[i,j] 
        d.append(l)
h=0
for i in range(len(d)-1):
    if prime(d[i][0]*d[i][1]):
        h+=1
        del d[i]
    
print(len(d))