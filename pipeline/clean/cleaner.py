   
def clean_data(json_obj):
    for key, value in json_obj.items():
        if(str(key) != "organization"):
            if(type(value).__name__ == "list"):
                result = _split_multiple_entry(value)
                
                new_arr = []

                for j in result:
                    j = _remove_spaces(j)
                    j = _capitalize_letters(j)
                    
                    new_arr.extend([j])

                json_obj[key] = new_arr

            elif(type(value).__name__ == "dict"):
                json_obj[key] = clean_data(json_obj[key])

            elif(type(value).__name__ == "str"):
                result = _capitalize_letters(value)
                result = _remove_spaces(result)
                json_obj[key] = result
            else:
                continue
            

    return json_obj

def _capitalize_letters(word):
    word = word.capitalize()
    return word

def _split_multiple_entry(source_array):
    tmp_arr = []
    for i in source_array:
        i = i.split(",")

        tmp_arr.extend(i)

    return tmp_arr

def _remove_spaces(variable):
    if(type(variable).__name__ == "list"):
        new_arr = []
        for word in variable:
            word = word.strip()

            new_arr.extend([word])

        return new_arr

    else:
        variable = variable.strip()
        return variable    