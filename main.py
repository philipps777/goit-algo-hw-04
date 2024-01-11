
import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def timsort(arr):
    return sorted(arr)


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def sort_time(sort_function, array_size):
    time_taken = timeit.timeit(
        stmt=f"{sort_function.__name__}(data)",
        setup=f"from __main__ import {sort_function.__name__}, generate_random_array; data = generate_random_array({array_size})",
        number=100
    )
    print(f"{sort_function.__name__} час ({array_size} елементів): {time_taken}")


def main():
    sort_time(merge_sort, 100)
    sort_time(insert_sort, 100)
    sort_time(timsort, 100)

    sort_time(merge_sort, 500)
    sort_time(insert_sort, 500)
    sort_time(timsort, 500)

    sort_time(merge_sort, 1000)
    sort_time(insert_sort, 1000)
    sort_time(timsort, 1000)


if __name__ == "__main__":
    main()


# merge_sort час (100 елементів): 0.02481351885944605
# insert_sort час (100 елементів): 0.0021056756377220154
# timsort час (100 елементів): 0.002124213707447052
# merge_sort час (500 елементів): 0.15167656354606152
# insert_sort час (500 елементів): 0.017274742014706135
# timsort час (500 елементів): 0.004080493003129959
# merge_sort час (1000 елементів): 0.3357028588652611
# insert_sort час (1000 елементів): 0.05815621744841337
# timsort час (1000 елементів): 0.009730834513902664


# merge_sort час (100 елементів): 0.032411737367510796
# insert_sort час (100 елементів): 0.04449028708040714
# timsort час (100 елементів): 0.010567714460194111
# merge_sort час (1000 елементів): 0.448945302516222
# insert_sort час (1000 елементів): 8.682091460563242
# timsort час (1000 елементів): 0.10791026335209608
# merge_sort час (5000 елементів): 2.73489582631737
# insert_sort час (5000 елементів): 117.53192273713648
# timsort час (5000 елементів): 0.5641792425885797
