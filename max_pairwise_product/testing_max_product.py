import random
from solution1 import max_product
from faster_method import max_product_faster

def stress_test(N, max_value):
    while True:
        n = random.randint(2, N)
        a = [random.randint(0, max_value) for _ in range(n)]
        print(a)
        result1 = max_product(a)
        result2 = max_product_faster(a)
        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: ", result1, result2)
            break

stress_test(5, 9)