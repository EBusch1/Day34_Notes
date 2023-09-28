# Day 34 Notes
# We can declare the varaible type when creating a variable
# age: int
# name: str
# height: float
# is_hooman: bool

# We can also declare types in functions
# We can ALSO declare the function output type
# Holy moly
def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False
    # # These pre-error messages are called TYPE HINTS
    # return "eek"
    return can_drive


if police_check(20):
    print("Move along.")
else:
    print("WASTED")
