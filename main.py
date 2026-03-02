import matplotlib.pyplot as plt

fib_counter = 0
#prints fibanacci sequence of k value recursively
def fibrecur(k):
    global fib_counter

    if k == 1:
        return 1
    if k == 2:
        return 1
    else:
        fib_counter += 1
        return fibrecur(k-1) + fibrecur(k-2)

#gcd of two nums using euclidean algorithm recursively
gcd_mod_counter = 0
def GCD(m, n):
    global gcd_mod_counter
    if n == 0:
        return m
    else:
        gcd_mod_counter += 1
        return GCD(n, m % n)

#using fibanacci function calculates operations in worst case of gcd which is when the two numbers are consecutive fibanacci numbers
def GCDworstcase(k):
    global gcd_mod_counter
    m = fibrecur(k+1)
    n = fibrecur(k)

    gcd_mod_counter = 0
    g = GCD(m, n)
    return g


#counts num of multiplications, algorithmn fromn canvas for next 3 functions  
exp1_counter = 0
def exp(a,n):
    global exp1_counter
    if n == 0:
        return 1
    exp1_counter += 1
    return exp(a, n-1) * a

exp2_counter = 0
def exp2(a, n):
    global exp2_counter
    if n == 0:
        return 1
    if n % 2 == 0:
        exp2_counter += 1
        return exp2(a, n//2) ** 2
    else:
        exp2_counter += 2
        return a *exp2(a, (n-1)//2) ** 2
    
exp3_counter = 0
def exp3(a, n):
    global exp3_counter
    if n == 0:
        return 1
    if n % 2 == 0:
        exp3_counter += 1
        return exp3(a, n//2) * exp3(a, n//2)
    else:
        exp3_counter += 2
        return a * exp3(a, (n-1)//2) * exp3(a, (n-1)//2)
    #part 1 of the project calulates num of additions for fibanacci and num of modulo operations for gcd and creates scatterplots for both
def part1():
    k_values = []
    fib_values = []
    gcd_values = []
    
    print("k\tfib_counter\tgcd_mod_counter")
    for k in range(1, 21):
        global fib_counter
        fib_counter = 0
        fibrecur(k)
        fib_add = fib_counter

        fib_counter = 0     
        global gcd_mod_counter
        gcd_mod_counter = 0
        GCDworstcase(k)

        print(f"{k}\t{fib_add}\t{gcd_mod_counter}")
        k_values.append(k)
        fib_values.append(fib_add)      
        gcd_values.append(gcd_mod_counter)

    #da scatterplot for fib counter
 
    plt.scatter(k_values, fib_values , color='blue', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("Fibonacci Counter vs k")
    plt.xlabel("K")
    plt.ylabel("# OF ADDITIONS")
    plt.show()
    #CLOSE THE PREVIOUS PLOT TO SEE THE NEXT PLOT
    #scatterplot for gcd mod counter
    plt.scatter(k_values, gcd_values , color='red', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("GCD Modulo Counter vs k")    
    plt.xlabel("K")
    plt.ylabel("# OF MODULO OPERATIONS")
    plt.show()    
#part 2 of the project calculates num of multiplications for 3 different algorithms for exponentiation and creates scatterplots for all 3 algorithms
def part2():
    #arrays of values for scatterplots 
    n_values = []
    exp1_values = []
    exp2_values = []
    exp3_values = []

    print("n\texp1\t\texp2\t\texp3")
    for n in range(0, 21):
        global exp1_counter, exp2_counter, exp3_counter
        exp1_counter = 0
        exp2_counter = 0  
        exp3_counter = 0

        exp(2, n)
        exp1_val = exp1_counter
        exp2(2, n)
        exp2_val = exp2_counter
        exp3(2, n)
        exp3_val = exp3_counter

        print(f"{n}\t{exp1_val}\t\t{exp2_val}\t\t{exp3_val}")
        n_values.append(n)
        exp1_values.append(exp1_val)
        exp2_values.append(exp2_val)
        exp3_values.append(exp3_val)
    #scatterplot for exp1
    plt.scatter(n_values, exp1_values , color='blue', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("exp1 Counter vs n")
    plt.xlabel("n")
    plt.ylabel("# OF MULTIPLICATIONS")
   
    #scatterplot for exp2
    plt.scatter(n_values, exp2_values , color='red', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("exp2 Counter vs n")  
    plt.xlabel("n")
    plt.ylabel("# OF MULTIPLICATIONS")

    #scatterplot for exp3
    plt.scatter(n_values, exp3_values , color='green', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("exp3 Counter vs n")    
    plt.xlabel("n")
    plt.ylabel("# OF MULTIPLICATIONS")
    plt.show()

def main():
    # print(exp(2, 10))
#un comment the part you want to run
    # part1()
    # part2()
    #Task 1: User is prompted for the value of k; program outputs the value 
    # of Fib(k) and GCD(m, n) where m = Fib(k+1) and n = Fib(k) .
    choice = input("User mode:\n 1. UserTestMode\n 2. ScatterPlotMode\n Enter 1 or 2: ")
    if choice == "1":
        k = int(input("Enter value of k: "))
        m = fibrecur(k+1)
        n = fibrecur(k)
        print("Fib(k): ", n)
        print("GCD(m, n): ", GCD(m, n))

        #Task 2: User is prompted for the value of a and n.;\1
        #program outputs the value an using each of the three algorithms.
        a = int(input("Enter value of a: "))
        n = int(input("Enter value of n: "))
        global exp1_counter, exp2_counter, exp3_counter
        exp1_counter = 0
        exp2_counter = 0  
        exp3_counter = 0

        print("test")
        result1 = exp(a, n)
        print(f"exp(a, n) using algorithm 1: {result1}, multiplications: {exp1_counter}")

        result2 = exp2(a, n)
        print(f"exp(a, n) using algorithm 2: {result2}, multiplications: {exp2_counter}")

        result3 = exp3(a, n)
        print(f"exp(a, n) using algorithm 3: {result3}, multiplications: {exp3_counter}")
    if choice == "2":
        part1()
        part2()

    
if __name__ == "__main__":
    main()