from random import randint
import time


def binary_search(ele, arr, i, j):
    if i <= j:
        m = (i + j) / 2
        if arr[m] == ele:
            return m
        else:
            if ele < arr[m]:
                return binary_search(ele, arr, i, m - 1)
            else:
                return binary_search(ele, arr, m + 1, j)
    else:
        return -1


def randomized_binary_search(ele, arr, i, j):
    if i <= j:
        m = randint(i, j)
        if arr[m] == ele:
            return m
        else:
            if ele < arr[m]:
                return randomized_binary_search(ele, arr, i, m - 1)
            else:
                return randomized_binary_search(ele, arr, m + 1, j)
    else:
        return -1


def create_arrays(size):
    i = 0
    n = 0
    arr = []
    members = []
    non_members_temp = []
    non_members_count = 0
    members_count = 0

    member_gap = size / 700

    while i < size:
        if randint(0, 1):
            arr.append(n)
            if members_count < 700 and i % member_gap == 0:
                members.append(n)
                members_count += 1
            i += 1
        else:
            non_members_temp.append(n)
            non_members_count += 1
        n += 1

    while non_members_count < 300:
        if randint(0, 1):
            non_members_temp.append(n)
            non_members_count += 1
        n += 1
    non_member_gap = len(non_members_temp) / 300
    non_members = [non_members_temp[i * non_member_gap] for i in range(300)]

    return arr, non_members, members


for k in range(5, 8):

    arr_size = 10 ** k

    print("Test " + str(k - 4) + "...................")
    print("")

    arr, non_members, members = create_arrays(arr_size)

    print('Array[:100] : ' + str(arr[:100]))
    print('Non Members : ' + str(non_members))
    print('Members : ' + str(members))
    print("")

    # ..................Binary Search.................................
    start_time = time.time()
    for m in members:
        binary_search(m, arr, 0, arr_size - 1)

    for nm in non_members:
        binary_search(nm, arr, 0, arr_size - 1)
    end_time = time.time()

    print("Binary Search(N = " + str(arr_size) + ") - Time(microseconds) : " + str(
        1000000 * (end_time - start_time) / 1000))
    print("")

    # ..................Randomized Binary Search.................................
    start_time = time.time()
    for m in members:
        randomized_binary_search(m, arr, 0, arr_size - 1)

    for nm in non_members:
        randomized_binary_search(nm, arr, 0, arr_size - 1)
    end_time = time.time()

    print("Randomized Binary Search(N = " + str(arr_size) + ") - Time(microseconds) : " + str(
        1000000 * (end_time - start_time) / 1000))
    print("")
