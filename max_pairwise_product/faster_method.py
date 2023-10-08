def max_product_faster(numbers : list[int]):
    index1 = -1
    for i in range(len(numbers)):
        if index1 == -1 or numbers[i] > numbers[index1]:
            index1 = i

    index2 = -1
    for j in range(len(numbers)):
        if j != index1 and (index2 == -1 or numbers[j] > numbers[index2]):
            index2 = j
    
    return numbers[index1] * numbers[index2]

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    print(max_product_faster(input_numbers))