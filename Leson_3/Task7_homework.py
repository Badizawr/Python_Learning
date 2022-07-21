st = input('Введите текст ->').lower().split()
d = {a: st.count(a) for a in set(st)}
for k, v in d.items():
    print(k, v)