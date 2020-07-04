from sys import argv , exit

def collatz(n):
    while n > 1:
        print(n, end = ', ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1
    print(n, end='\n\n')

if __name__ == "__main__":
   
    if len(argv) == 1:
        print(f"Usage: python {argv[0]} integer")
        exit(1)

    for n in argv[1:]:
        try:
            n = int(n)
            if n <= 0:
                raise ValueError
            collatz(int(n))
        except ValueError:
            print(f"{n} is not a valid positive integer.")