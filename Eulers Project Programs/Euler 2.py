def fibonacci():
    fib_sequence = [1, 2]
    while fib_sequence[-2] < 4000000:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def even(fibonacci,sum):
    for i in fibonacci:
        if i%2==0:
            sum=i+sum
    return sum

sum=0
print(even(fibonacci(),sum))