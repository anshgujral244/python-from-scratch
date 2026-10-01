# A function is a reusable block of code that performs a task.
def greet(name):
    # The name parameter receives the value passed to the function.
    print(f"Hello, {name}!")


# Call the function with an argument.
greet("Ansh")


def add(first_number, second_number):
    # return sends a result back to the code that called the function.
    return first_number + second_number


# Store and display the returned result.
total = add(5, 3)
print(total)


def describe_pet(name, animal="dog"):
    # Default parameter values are used when an argument is not provided.
    print(f"{name} is a {animal}.")


# Pass one argument and use the default animal value.
describe_pet("Buddy")

# Keyword arguments make each value's purpose clear.
describe_pet(name="Milo", animal="cat")
