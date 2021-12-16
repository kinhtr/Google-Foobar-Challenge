#Write a function to assign a 5 consecutive prime numbers as id for workers with index number is given
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(index):
    n = 2
    s = ""
    while len(s) <= index + 4:
        if isPrime(n):
            s += str(n)
        n += 1
    return s[index:index+5]
