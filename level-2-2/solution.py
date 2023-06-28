def solution(height, converters):
    if (height < 1 or height > 30):
        print("Invalid height, please enter a height between 1 and 30")
        return

    converter_count = len(converters)

    if (converter_count < 1 or converter_count > 10000):
        print("Invalid number of converters, please enter between 1 and 10000 converters")
        return
    
    # Initialize a list to store the parent converters
    parents = []

    original_h = height

    # Iterate over the converters in q
    for converter in converters:
        # The label of the root converter
        root = 2 ** height - 1
        print(f"Root: {root}")

        # If the converter is the root, it has no parent
        if converter == root:
            parents.append(-1)
            continue

        # The label of the current parent converter
        current_parent = root

        # Find the parent converter
        while height > 1:
            # The label of the left and right child converters
            left_child = current_parent - 2 ** (height - 1)
            right_child = current_parent - 1
            print(f"Current Parent: {current_parent}, Left Child: {left_child}, Right Child: {right_child}")

            # If the converter is a left or right child, we have found its parent
            if converter == left_child or converter == right_child:
                parents.append(current_parent)
                break

            # If the converter is in the left subtree, move to the left
            if converter < left_child:
                current_parent = left_child
            # If the converter is in the right subtree, move to the right
            else:
                current_parent = right_child

            height -= 1

        height = original_h

    # Return the parent converters
    return parents


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