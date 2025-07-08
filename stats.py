def count_words(text):
    split_text = text.split()
    return len(split_text)

def count_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        characters[char] = characters.get(char, 0) + 1
    return characters

def sort_on(items):
    return items["num"]

def sort_character_dict(char_dict):
    sorted_dict = []
    for char,num in char_dict.items():
        sorted_dict.append({"char": char, "num": num})
    return sorted(sorted_dict, reverse=True, key=sort_on)
