Year=int(input())
check_luna=0
if Year%4==0:
    check_luna =1
    if Year%100==0:
        check_luna=0
        if Year%400==0:
            check_luna=1
        else:
            check_luna=0        
    else :
        check_luna=1
else :
    check_luna=0
print(check_luna)


    