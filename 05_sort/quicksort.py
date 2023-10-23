def sort(lst):
    if len(lst) <= 1:
        return lst
    
    ref = lst[0]
    sm, eq, lg = [], [], []
    
    for el in lst:
        if el < ref:
            sm.append(el)
        elif el == ref:
            eq.append(el)
        else:
            lg.append(el)
        
    return sort(sm) + eq + sort(lg)



sortiert = sort([3, 2, 6, 1, 5])
print(sortiert)                     # -> [1, 2, 3, 5, 6]

assert sort([]) == []
assert sort([19]) == [19]
assert sort([1, 2, 3]) == [1, 2, 3]
assert sort([3, 6, 1, 4]) == [1, 3, 4, 6]


# Code für die Zeitmessung
import random
import time

size = 1_000

lst = list(range(size))
random.shuffle(lst)   # lst ist jetzt gemischelt
start_time = time.perf_counter()
lst = sort(lst)
end_time = time.perf_counter()
difference = end_time - start_time
print(f"Grösse: {size}, Zeitdauer: {difference:.5} s")

# Haben wir auch wirklich korrekt sortiert?
assert lst == list(range(size))
