def dictionary_converter(array):
    return {arr: index_list for arr in array for index_list in
            [[idx for idx, value in enumerate(array) if value == arr] for i in range(len(array))]}


def jaccard(first_set, second_set):
    intersection_count = 0
    union_count = len(first_set) + len(second_set)
    for elem in first_set:
        if elem in second_set:
            intersection_count += 1
            union_count -= 1
    jaccard_similarity = intersection_count / union_count
    return jaccard_similarity


if __name__ == '__main__':
    in_array = input("Input array: ").split(" ")
    print(dictionary_converter(in_array))
    print(jaccard({1, 2, 3, 4, 5}, {1, 2, 3, 6, 7, 8, 9}))