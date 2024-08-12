# a = [1, 3, 43, 23 ,32, 32, 32, 32, 23, 21, 324, 23, 56]
# print([i ** 2 if i % 2 == 0 else i ** 3 for i in a] )


# a = {i: i ** 2 for i in range(1, 11)}
# print(a)

# print([i ** 2 if i % 2 ==0 else i - 1 for i in range(1, 11)])

# a = {1: 'b', 4: 'e', 2: 'b', 3: 'c'}
# s = dict(sorted(a.items()))
# print(s)


# a = {1: 23, 2: 32, 3: 45, 4: 21}
#
# s = {i: j ** 2 if j % 2 == 0 else j for i, j in a.items()}
# print(s)


# a = [23, 32, 32, 32, 23, 32, 32, 'Hallo', True, False]
# s = [
#     i ** 2 if isinstance(i, (int, float)) and not isinstance(i, bool) and i % 2 == 0
#     else i ** 0.5 if isinstance(i, (int, float)) and not isinstance(i, bool) and i % 2 != 0
#     else i
#     for i in a
# ]
# print(s)
