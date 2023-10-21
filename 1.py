students = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

full_names = [student['full_name'] for student in students]
split_names = [name.split() for name in full_names]
fio_list = [' '.join(split_name) for split_name in split_names]

result = ',\n'.join(fio_list)
print(result)
