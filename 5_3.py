

# translate = {
#     "red": "rojo",
#     "blue": "aloz",
#     "green": "verdi",
#     "white": "blanco",
# }

# alist = [
#     "rojo",
#     "aloz",
#     "verdi",
#     "blanco"
# ]


# print("alist", alist[1])
# print("translate red", translate["white"])

user = {
    "first_name": "Robert",
    "last_name": "Smith",
    "age": 19,
    "school": {
        "school_name": "Fresno State",
        "grade": "Senior",
        "gpa": 3.5,
        "completed_courses": [
            "Programming Fund",
            "Project Management",
            "Psychology"
        ]
    }
}

# print(user["first_name"] + "'s age is: ", user["age"])
# print("courses", user["school"]["completed_courses"])
# num_courses = len(user["school"]["completed_courses"])
# output = user["first_name"] + " goes to " + user["school"]["school_name"] + " and is taking " + str(num_courses) + " classes."

# print(output)

# if "completed_courses" in user:
#     print("True")
# else:
#     print("False")

# print("Original user: ", user)
# user["school"] = None
# print("Mutated user: ", user)

# school = user.get("school", None)

# print("School", school.get("completed_courses"))

# print("keys: ", user.keys())
# print("Values: ", user.values())

# user_data = list(user)

# print("User dictionary converted into a list: ", user_data)
# print("User dictionary converted into a tuple of key value pairs: ", user.items())

# print("User", user)
# alist = [1, 2]

# aset = set(alist)

# del user["school"]

# print("User with no school: ", user)

# user.clear()

# print("Cleared user object: ", user)
original_dict = {}
dict1 = {
    "a": "A",
    "b": "B",
    "c": "C"
}

dict2 = {
    "c": "C",
    "d": "D",
    "e": "E",
}

# print("Merged Dictionary", original_dict.update(dict2)) # TODO: check python version

def main():
    print("Main running...")
    d = {}
    print(d)

    d.update(dict2)
    print("d", d)

    print("Keys", d.keys())
    print("Values", d.values())
main()