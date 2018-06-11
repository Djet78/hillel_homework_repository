# ----------------------- task 12 ------------------------

from random import randint


def generate_examples():
    """
    Generate given amount of examples w/o repetitions and multiplying on 1 and 10. But no more than 36!
    :return: Set. of examples
    """
    examples_to_output = set({})
    unique_examples = []
    for i in range(2, 9 + 1):
        for i2 in range(i, 9 + 1):
            unique_examples.append(str(i) + "*" + str(i2))
    while len(examples_to_output) < 15:
        examples_to_output.add(unique_examples[randint(0, len(unique_examples) - 1)])
    return examples_to_output


print(generate_examples())
