def sum_of_the_squares1(n):

    if not (isinstance(n,int) and n > 0):
        print("Please enter a positive integer!")
        quit()

    sum = 0

    for i in range(1,n):
        sum += i**2

    return sum

print(sum_of_the_squares1(5))