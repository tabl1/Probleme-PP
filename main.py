# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('citire.txt') as file :
        x = file.read()

    x = x.replace('!', '')
    x = x.replace('?', '')
    x = x.replace('.', '')
    x = x.replace(',', '')
    x = x.replace(':', '')
    x = x.replace(';', '')
    x = x.replace('\'', '')
    x = x.replace('\"', '')

    aux_string = ''
    for element in x:
        if element == 'a':
            aux_string = aux_string + element.upper()
        else:
            aux_string = aux_string + element

    aux_string2 = ""
    for element in x:
        if element != ' ':
            aux_string2 = aux_string2 + element

    print(str(aux_string))
    print(str(aux_string2))

    file.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/