#!//Users/cemakay/Python/.venv/bin/python3


def ratio(arr):
    n = len(arr)

    pos_count = len([+1 for num in arr if num > 0])
    neg_count = len([+1 for num in arr if num < 0])
    zero_count = len([+1 for num in arr if num == 0])
    # print(f'Positive count: {pos_count}')
    # print(f'Negative count: {neg_count}')
    # print(f'Zero count: {zero_count}')

    # print(f'Positive ratio:', "{:.6f}".format(pos_count/n))
    # print(f'Negative ratio:', "{:.6f}".format(neg_count/n))
    # print(f'Zero ratio:', "{:.6f}".format(zero_count/n))
    print("{:.6f}".format(pos_count/n))
    print("{:.6f}".format(neg_count/n))
    print("{:.6f}".format(zero_count/n))
    


arr = [1, 3, 5, 7, 6, 0, 0, -8, -4, 0, -1]

ratio(arr)
