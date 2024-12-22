from actions import Actions

def menu():
    print("Welcome to the movie collection manager.\nPlease choose an action:")
    for action in Actions:
        print(f"{action.name} - {action.value}")
    return input("Your selection:\n")
