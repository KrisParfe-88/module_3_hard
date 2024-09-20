def calculate_structure_sum(data):
    total = 0
    for i in data:
        if isinstance(i, (int, float)):
            total += i
        elif isinstance(i, str):
            total += len(i)
        elif isinstance(i, (list, tuple, set)):
            total += calculate_structure_sum(i)
        elif isinstance(i, dict):
            for key, value in i.items():
                total += calculate_structure_sum([key])
                total += calculate_structure_sum([value])
    return total


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
