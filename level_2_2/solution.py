def solution(target_height, converters):
    if (target_height < 1 or target_height > 30):
        print("Invalid height, please enter a height between 1 and 30")
        return

    converter_count = len(converters)

    if (converter_count < 1 or converter_count > 10000):
        print("Invalid number of converters, please enter between 1 and 10000 converters")
        return
    
    # Initialize a list to store the parent converters
    result_converters = []

    root_height = target_height

    # Iterate over the converters in q
    for converter in converters:
        # The label of the root converter
        root = 2 ** target_height - 1

        # If the converter is the root, it has no parent
        if converter == root:
            result_converters.append(-1)
            continue

        target_root = root

        while target_height > 1:
            # Calculate the left and right child of the current parent converter
            left = target_root - 2 ** (target_height - 1)
            right = target_root - 1

            # If the converter is a left or right child, we have found its parent
            if converter == left or converter == right:
                result_converters.append(target_root)
                break

            if converter < left:
                target_root = left
            else:
                target_root = right

            target_height -= 1

        target_height = root_height

    return result_converters


print(solution(5, [19, 14, 28]))
# print(solution(5, [22]))
# print(solution(3, [7, 3, 5, 1]))
# print(solution(5, [19, 14, 28, 1, 2, 3, 4, 5, 6, 7, 8]))
# print(solution(5, [19, 14, 28, 1, 2, 3, 4, 5, 6, 7, 8, 31]))
# print(solution(5, [19, 14, 28, 1, 2, 3, 4, 5, 6, 7, 8, 0]))

# # Negative tests
# print(solution(0, [1, 1]))
# print(solution(31, [1, 1]))
# print(solution(3, []))
# print(solution(3, [0, 1]))
# print(solution(3, [1, 2 ** 3]))