from StorageManager import FileController

def result_voting():

    list=FileController.get_voting_list()

    print len(list)

    if len(list) == 1:
        difficulty = 32
        return difficulty
    elif len(list) == 2:
        difficulty = 31
        return difficulty
    elif len(list) == 3:
        difficulty = 30
        return difficulty
    elif len(list) == 4:
        difficulty = 26
        return difficulty
    elif len(list) == 5:
        difficulty = 21
        return difficulty
    elif len(list) == 6:
        difficulty = 11
        return difficulty
    else:
        return False
