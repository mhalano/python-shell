from os import system


while True:

    try:
        command = input("$ ")
    except KeyboardInterrupt:
        exit(1)

    if command == "exit" or command == "quit":
        print("Hasta la vista, baby!")
        exit(0)
    else:
        system(command)


