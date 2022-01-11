# String
string_var = "hello"

# to string
print("str function " + str(60))

# Interpolate number and variable in print()
print(f"Interpolating string {20}, {string_var}")

# Integer
integer_var = 2

# Float
float_var = 2.1


# Function
def say_hello(target):
    print(f"{string_var} {target}")


say_hello("Venus")




# User input
user_input = input("Please enter a number\n")

print(f"You have entered {user_input}")