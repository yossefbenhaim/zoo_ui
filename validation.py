

def validation(json,animal):
    if check_file_json(json)==True:
        if check_k(animal)==True:
            if check_v(animal) == True:
                return True
            return check_v(animal)
        return check_k(animal)
    return "not good json"


def check_k(animal):

    validation_animal = dict({
        "name_of_zoo": "",
        "name_of_animal": "",
        "family": "",
        "hungry": "",
        "age": ""
    })

    for i in validation_animal:
        if i not in animal:
            return f'not good key most be like : {i}  '
    return True

def check_v(animal):
    if type(animal["name_of_zoo"]) is not str:
        return f'name_of_zoo : most be string'
    if type(animal["name_of_animal"]) is not str:
        return f'name_of_animal : most be string'
    if type(animal["family"]) is not str:
        return f'family : most be string'
    if type(animal["hungry"]) is not bool:
        return f'hungry : most be boolean'
    if type(animal["age"]) is not int:
        return f'age : most be number'
    return True




def check_file_json(is_json):

     if is_json:
        return True
     else:
         return "not good file json"



