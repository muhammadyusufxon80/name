
# def pow(n1, n2):
#     return n1 ** n2
#
# def run(func, num1, num2):
#     print(func)
#     print(func(num1, num2))
#
# run(pow, 2, 4)






# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are awesomest!"
#
# def great_bob(greeter_func):
#     return greeter_func("Bob")
#
# print(great_bob(say_hello))
# print(great_bob (be_awesome))







# def parent():
#     print("printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first_child() function")
#
#     def second_child():
#         print("Printing from the second_child() function")
#
#     second_child()
#     first_child()
#
# print(parent())
















#
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child

# first_child = parent(1)
# second_child = parent(2)
#
# print(first_child())
# print(second_child())
#
                    # print(parent(1)())
                    # print(parent(2)())













#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
# # say_whee = my_decorator(say_whee)
# # print(say_whee())












#
#
def outer_func():
    var = 100

    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        print(f"Printing another_var from inner_func(): {another_var}")

    another_var = 200  # This is defined after calling inner_func()
    inner_func()
    print(f"Printing var from outer_func(): {var}")


outer_func()



