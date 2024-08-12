# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Something is happening before the function is called.')
#         result = func(*args, **kwargs)
#         print('Something is happening after the function is called.')
#         return result
#     return wrapper
#
#
# # @my_decorator
# # def say_hello(*, name: str) -> None:
# #     print(f'Hello!, {name}!')
#
#
# # say_hello(name='Killer')
#
#
# @my_decorator
# def add_number(*, a: int, b: int) -> int:
#     print('Adding numbers...')
#     return a + b
#
#
# result = add_number(a=2, b=3)
# print(result)








