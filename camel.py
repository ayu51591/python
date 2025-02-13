def camel_to_snake(camel_case):
    snake_case = ""
    for i in camel_case:
        if i.isupper():
            snake_case += "_" + i.lower()
        else:
            snake_case += i
    return snake_case.lstrip("_")  

camel_case = input("camelCase: ")
snake_case = camel_to_snake(camel_case)
print("snake_case:", snake_case)