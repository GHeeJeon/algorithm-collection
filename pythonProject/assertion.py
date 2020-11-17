def assert_sorted(collection, comparator):
    for i in range(len(collection) - 1):
        left = collection[i]
        right = collection[i + 1]

        if not comparator(left, right):
            raise Exception("FUCK!!!!!!")

    print("The collection is well sorted.")