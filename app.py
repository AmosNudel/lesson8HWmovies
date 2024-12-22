from actions import Actions
from menu import menu
import actions_handler

if __name__ == "__main__":
    while True:
        try:
            action = Actions(int(menu()))
            if action == Actions.EXIT:
                print("Goodbye!")
                exit()
            if action == Actions.ADD:
                actions_handler.add()
            if action == Actions.DISPLAY:
                actions_handler.display()
            if action == Actions.DELETE:
                actions_handler.delete()
            if action == Actions.FIND:
                actions_handler.find()
        except ValueError:
            print("Please enter a number within range")
