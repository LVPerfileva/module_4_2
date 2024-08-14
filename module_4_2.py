def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()  # PyCharm не может найти функцию в глобальном пространстве, так как она  в
# объемлющем пространстве test_function