import matplotlib.pyplot as plt


fib_counter = 0
## Calculates the fibonacci sequence recursively and counts the number of additions.
def fibrecur(k):
    global fib_counter
    if k <= 2:
        return 1
    result = fibrecur(k-1) + fibrecur(k-2)
    fib_counter += 1  
    return result

## Calculates the greatest common divisor of two numbers using the Euclidean algorithm recursively and counts the number of modulo operations.
def GCD(m, n):
    if n == 0:
        return m
    else:
        global gcd_mod_counter
        gcd_mod_counter += 1
        return GCD(n, m % n)

## Using fibanacci function calculates operations in worst case of gcd which is when the two numbers are consecutive fibonacci numbers
def GCDworstcase(k):
    global gcd_mod_counter
    m = fibrecur(k+1)
    n = fibrecur(k)

    gcd_mod_counter = 0
    g = GCD(m, n)
    return g

exp1_counter = 0
## Decrease-by-one Algorithm w/ an additional counter for the number of multiplications.
def exp(a,n):
    global exp1_counter
    if n == 0:
        return 1
    exp1_counter += 1
    return exp(a, n-1) * a

exp2_counter = 0
## Decrease-by-constant-factor Algorithm w/ an additional counter for the number of multiplications.
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
## Divide-and-Conquer Algorithm w/ an additional counter for the number of multiplications.
def exp3(a, n):
    global exp3_counter
    if n == 0:
        return 1
    if n % 2 == 0:
        half = exp3(a, n // 2)
        exp3_counter += 1
        return half * half
    else:
        half = exp3(a, (n - 1) // 2)
        exp3_counter += 2
        return a * half * half

## SelectionSort Alogorithm w/ an additional counter for the number of comparisons.
def selectionSort(mylist):
    comparisons = 0

    n = len(mylist)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if mylist[j] < mylist[min_index]:
                min_index = j
        min_value = mylist.pop(min_index)
        mylist.insert(i, min_value)

    return comparisons 

## InsertionSort Alogorithm w/ an additional counter for the number of comparisons.
def insertionSort(arr):
    comparisons = 0

    n = len(arr)
    
    if n <= 1:
        return 0
    for i in range(1, n):
        key = arr[i]         
        j = i - 1
        while j >= 0 and key < arr[j]: 
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        comparisons += 1
        arr[j + 1] = key
    
    return comparisons

## Plots two scatterplots; one for num of additions on FIB Sequence , one for num of modulo operations on GCD.
def part1():
    k_values = []
    fib_values = []
    fib_n_values = []
    gcd_values = []
    
    for k in range(1, 30):
        global fib_counter, gcd_mod_counter
        fib_counter = 0
        fib_k = fibrecur(k)
        fib_add = fib_counter

        fib_counter = 0     
        gcd_mod_counter = 0
        GCDworstcase(k)

        k_values.append(k)
        fib_values.append(fib_add)   
        fib_n_values.append(fib_k)   
        gcd_values.append(gcd_mod_counter)
 
    plt.scatter(k_values, fib_values , color='blue', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("Fibonacci Counter vs k")
    plt.xlabel("K")
    plt.ylabel("# OF ADDITIONS")
    plt.show()

    plt.scatter(fib_n_values, gcd_values , color='red', marker='o', s=100, alpha=0.7, edgecolors='black')
    plt.title("GCD Modulo Counter vs n")    
    plt.xlabel("n = Fib(k)")
    plt.ylabel("# OF MODULO OPERATIONS")
    plt.show()    

## Plots a scatterplot for the Number of Multiplications for 3 different algos of exponentiation.
def part2():
    # Arrays of values for scatterplots 
    n_values = []
    exp1_values = []
    exp2_values = []
    exp3_values = []

    print("n\texp1\t\texp2\t\texp3")
    for n in range(0, 60):
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

    plt.scatter(n_values, exp1_values , color='blue', marker='o', s=100, alpha=0.7, edgecolors='black', label='Decrease-by-one')
    plt.scatter(n_values, exp3_values , color='green', marker='o', s=100, alpha=0.7, edgecolors='black', label='Divide-and-Conquer')
    plt.scatter(n_values, exp2_values , color='red', marker='x', s=100, alpha=0.7, edgecolors='black', label='Decrease-by-constant-factor')
    plt.xlabel("n")
    plt.ylabel("# OF MULTIPLICATIONS")
    plt.legend(['Decrease-by-one', 'Divide-and-Conquer', 'Decrease-by-constant-factor'])
    plt.title("Multiplications M(n) vs n")
    plt.show()

## Plots the scatterplots for the sorting algorithms.
def plotSorting(firstval, secondval, thirdVal, fourthVal, case_name):
    plt.figure(figsize=(12, 6))
    plt.scatter(firstval, secondval , color='blue', marker='o', s=100, alpha=0.7, edgecolors='black', label='Selection Sort')
    plt.scatter(thirdVal, fourthVal , color='green', marker='x', s=100, alpha=0.7, edgecolors='black', label='Insertion Sort')
    plt.title("number of comparisons C(n) for " + case_name + " Case")    
    plt.xlabel("n")
    plt.ylabel("# OF COMPARISONS")
    plt.legend()
    plt.xlim(0, 10500)  # x axis bounds
    plt.ylim(0, 50000000)
    plt.yticks(range(0, 50000000, 10000000))
    plt.xticks(range(0, 10500, 500))  # x axis increments
    plt.show()

## Builds an array of arrays for the sorting algorithms from testSet folder.
def buildArray(potentialvar):
    listOfArrays = []
    for num in range(500, 10500, 500):
        with open("data/testSet/data" + str(num) + potentialvar + ".txt", "r") as f:
            arr = [int(line.strip()) for line in f]
        listOfArrays.append(arr)
    return listOfArrays
        
## Runs the sorting algorithms on the arrays and plots the results.
def part3():
    data = [ "", "_sorted", "_rSorted"]
    case_names = ["Average", "Best", "Worst"]

    ## Interate through all array types
    for num in range(0, 3, 1):
        arr = buildArray(data[num])
        ## Make a copy as we need to use the same array for both sorting algorithms
        arr2 = [a.copy() for a in arr]

        selection_n, selection_comps = [], []
        insertion_n, insertion_comps = [], []

        for ar, ar2 in zip(arr, arr2):
            selection_n.append(len(ar))
            selection_comps.append(selectionSort(ar))
            insertion_n.append(len(ar2))
            insertion_comps.append(insertionSort(ar2))

        plotSorting(selection_n, selection_comps, insertion_n, insertion_comps, case_names[num])    

def main():
    choice = input("Enter 1 for UserTestMode or 2 for ScatterPlotMode: ")
    if choice == "1":

        # Task 1 
        k = int(input("Enter value for k: "))
        m = fibrecur(k+1)
        n = fibrecur(k)
        print(f"Fib({k}): ", n)
        print(f"GCD({m}, {n}): ", GCDworstcase(k))

        # Task 2
        a = int(input("Enter value of a: "))
        n = int(input("Enter value of n: "))
        global exp1_counter, exp2_counter, exp3_counter
        exp1_counter = exp2_counter = exp3_counter = 0
        print(f"Answer for: {a}^{n}:")
        print(f"Decrease-by-one: {exp(a, n)}")
        print(f"Decrease-by-constant-factor: {exp2(a, n)}")
        print(f"Divide-and-Conquer: {exp3(a, n)}")

        # Task 3
        n = int(input("Enter list size (10-100, increment 10): "))
        if n < 10 or n > 100 or n % 10 != 0:
            print("Invalid list size. Please enter a multiple of 10 between 10 and 100.")
            return
        with open(f"data/smallSet/data{n}.txt") as f:
            arr = [int(line.strip()) for line in f]
        arr2 = arr.copy()
        selectionSort(arr)
        insertionSort(arr2)
        print("Selection Sort result:", arr)
        print("Insertion Sort result:", arr2)
    else:
        part1()
        part2()
        part3()

if __name__ == "__main__":
    main()
    