def append_data(name_file, data):
    with open(name_file, 'a') as file:
        file.write(f"{data},")


def over_writing(name_file, data):
    with open(name_file, 'w') as file:
        file.write("")

    for i in data:
        with open(name_file, 'a') as file:
            file.write(f"{i},")