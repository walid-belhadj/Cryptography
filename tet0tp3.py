import sys, getopt, random

def fermat_primality(n):
    a = random.randint(0, n-1)
    if n <= 1:
        return False
    else:
        return a**(n-1) % n == 1
        
def random_prime(a, b):
    while True:
        n = random.randint(a,b)
        if fermat_primality(n):
            break
    return n

def main():	
	if(len(sys.argv) < 3):
		print "must provide min and max value"
		sys.exit()	
	min = int(sys.argv[1])
	max = int(sys.argv[2])
	print(random_prime(min, max))
		
main()