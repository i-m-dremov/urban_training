#Цель: закрепить знания о списочных и словарных сборках, решив несколько небольших задач.

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}

print(first_result)     # [10, 8, 8]
print(second_result)    # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'),
                        # ('Monitors', 'Computer'), ('Variable', 'Computer')]
print(third_result)     # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8,
                        # 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}
