
Directory = ["Home", "Documents", "Music", "Downloads", "Desktop" ]
current_directory = " "

while True:
    command = input(F"custom-cmd ~/{current_directory} ").lower()

    if (command == "q"): #end command
        break

    elif (command == "ls"): #ls command
        print(Directory)

    elif (command[0:5] == "mkdir"): #mkdir command
        add_directory = command[6:]
        Directory.append(add_directory)

    elif (command == "rmdir"): #rmdir command
        remove_directory = input("name of directory: ")
        Directory.remove(remove_directory)

    elif (command == "cd"): #cd command
        name_of_directory = input("name of directory: ")
        if name_of_directory in Directory:
            current_directory = name_of_directory

