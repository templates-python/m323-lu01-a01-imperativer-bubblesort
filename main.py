def sort(numbers):

    for j in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i + 1] = numbers[i+1], numbers[i]



if __name__ == '__main__':
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(numbers)
    sort(numbers)
    print(numbers)