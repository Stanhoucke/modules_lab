def user_choice():
    option = input("Select an option 1, 2, 3, 4, 5 or (Q)uit: ")
    return option


def user_desc():
    description = input("Enter task description to search for: ")
    return description


def user_time():
    time = int(input("Enter task duration: "))
    return time
