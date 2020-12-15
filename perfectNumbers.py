def perfectNumber(n):
    sum = 0
    for i in range(1, n):
        if(n % i == 0):
            sum = sum + i

    if (sum == n):
        return True
    else:
        return False

def main():
    print("all perfect numbers from 1 to 10.000: ")
    for i in range(1, 10000):
        if(perfectNumber(i)):
             print(" %d is a Perfect Number" %i)

    print("end of display")
    
        
main()