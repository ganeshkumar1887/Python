def fibonacci(num):
    series = [0,1]
    for i in range(2,num):
        series.append(series[-1]+series[-2])
    return series
def main():
    n=int(input("Enter the number of terms::"))
    print(f"Fibonacci series =",fibonacci(n))
main()