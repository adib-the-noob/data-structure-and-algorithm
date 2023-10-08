def max_product(numbers : list[int]):
    max_product = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            max_num = max(max_product, numbers[i]*numbers[j])
    return max_num

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(max_product(input_numbers))