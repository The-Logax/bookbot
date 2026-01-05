def get_num_words(text):                    # counts words in file
    words = text.split()
    num_words = len(words)
    return num_words

def get_num_characters(text):               # counts characters in file
    letters_dict = {}
    letters = text.lower()
    for letter in letters:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else: 
            letters_dict[letter] = 1    
    return letters_dict

def sort_on(character):                     # helper for below function
    return character["num"]

def dict_to_list(letters_dict):             # sorts list of counted characters
    num_list = []
    for letter in letters_dict:
        new_dict = {"char": letter, "num" : letters_dict[letter]}
        num_list.append(new_dict)
    
    num_list.sort(reverse=True, key=sort_on)
    return num_list