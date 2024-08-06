"""
Sortiert eine Liste von Zahlen aufsteigend
"""


def sort(numbers):
    """
    Sortiert eine Liste von Zahlen aufsteigend
    :param numbers:
    :return:
    """
    for _ in range(len(numbers)):
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i + 1] = numbers[i+1], numbers[i]



if __name__ == '__main__':
    num = [64, 34, 25, 12, 22, 11, 90]
    print(num)
    sort(num)
    print(num)
