GREETING = "Hello"


def greet(name):
    return f"{GREETING} {name}"


def farewell(name):
    return f"Bye {name}"


def shout_1789856247(name):
    return greet(name).upper()
