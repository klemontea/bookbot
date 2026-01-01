def count_words(texts: str):
    words = texts.split()
    return len(words)

def count_chars(texts: str):
    result = dict()

    for char in texts:
        char_lower = char.lower()

        if char_lower in result:
            result[char_lower] += 1
        else:
            result[char_lower] = 1

    return result

def sort_dicts(char_dicts: dict):
    char_num_dict_list = []
    for key, value in char_dicts.items():
        char_num_dict_list.append({"char": key, "num": value})

    def sort_on(items: dict):
        return items["num"]
        
    char_num_dict_list.sort(reverse=True, key=sort_on)
    return char_num_dict_list