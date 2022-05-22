poetry = """Szybko, zbudź się, szybko, wstawaj,
    Szybko, szybko, stygnie kawa,
    Szybko, zęby myj i ręce"""

poetry = poetry.replace(",", "")
poetry = poetry.lower()
words = poetry.split()

words_counter = {}

for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1

print(words_counter)

for k, v in words_counter.items():
    print(f'- {k} : {v}')