"""
Пример 1:
Израз: 1 or 1 and 0
Първо се изпълнява and → 1 and 0 = 0
След това or → 1 or 0 = 1 (True)
"""
print(1 or 1 and 0)


"""
Пример 2:
Израз: not 1 or 0 and 1
Приоритет: not → and → or
not 1 → False
0 and 1 → 0
False or 0 → False
"""
print(not 1 or 0 and 1)


"""
Пример 3:
Израз: False and True or False
False and True → False
False or False → False
"""
print(False and True or False)


"""
Пример 4:
Израз: not (1 and 0) and (False and True or False)
(1 and 0) → 0 → not 0 → True
(False and True) → False
False or False → False
True and False → False
"""
print(not (1 and 0) and (False and True or False))


"""
Пример 5:
Израз: not (not 1 and 0) and (False and True or False)
not 1 → False
(False and 0) → False
not False → True
(False and True) → False
False or False → False
True and False → False
"""
print(not (not 1 and 0) and (False and True or False))


"""
Пример 6:
Израз: not (not 1 and 0) or (False and True or False)
not 1 → False
(False and 0) → False
not False → True
(False and True) → False
False or False → False
True or False → True
"""
print(not (not 1 and 0) or (False and True or False))
