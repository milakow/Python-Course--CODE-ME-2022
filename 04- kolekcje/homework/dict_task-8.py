woman_names = {
    'Poland': ['Susanna', 'Juliet', 'Sophie', 'Hannah', 'Maya', 'Laura', 'Olivia', 'Alice', 'Lena', 'Pola'],
    'Spain': ['Lucía', 'Martina', 'Maria', 'Sophie', 'Paula', 'Daniela', 'Valeria', 'Alba', 'Juliet', 'Noa'],
    'Switzerland': ['Emma', 'Mia', 'Sophie', 'Lina', 'Lena', 'Lea', 'Lara', 'Emily', 'Nina', 'Anne'],
    'Italy': ['Sophie', 'Juliet', 'Aurora', 'Alice', 'Ginevra', 'Emma', 'Giorgia', 'Greta', 'Beatrice', 'Anne'],
    'Germany': ['Sophie', 'Marie', 'Maria', 'Mia', 'Sofia', 'Emma', 'Anne', 'Hannah', 'Johanna', 'Leonie'],
    'Netherlands': ['Sophie', 'Juliet', 'Lieke', 'Emma', 'Sanne', 'Anna', 'Lotte', 'Eva', 'Anne', 'Lisa'],
    'Finland': ['Maria', 'Sophie', 'Aurora', 'Emily', 'Olivia', 'Aino', 'Amanda', 'Ilona', 'Helmi', 'Matilda'],
    'Denmark': ['Emma', 'Sophie', 'Ida', 'Freya', 'Clara', 'Laura', 'Anna', 'Ella', 'Isabella', 'Karla'],
    'Belgium': ['Emma', 'Olivia', 'Louise', 'Mila', 'Alice', 'Elise', 'Lina', 'Juliet', 'Sophie', 'Lucy'],
    'Norway': ['Emma', 'Norah', 'Olivia', 'Sarah', 'Emily', 'Leah', 'Sophie', 'Ella', 'Amaile', 'Maya']
}

# just_names = woman_names.values()
# list_from_dict = list(woman_names.values())
# print(just_names)

names = []
for value in woman_names.values():
    names.extend(value)
print(names)
print(len(names))

name_counter = []

for name in names:
    if names.count(name) > 3:
        name_counter.append(name)
set_name = set(name_counter)
print(set_name)


