
def return_evens(num_list):
    list = [i for i in num_list if i%2==0]
    return list
    pass

def make_exclamation(sentence_list):
    if sentence_list == []:
        return []
    generator = (eachsentence + "!" for eachsentence in sentence_list)
    return list(generator)
    pass