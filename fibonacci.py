def fibonacci(n):
    counter=1
    before=counter
    for i in range(n):
        before=counter-before
        print(counter)
        counter+=before

fibonacci(9)