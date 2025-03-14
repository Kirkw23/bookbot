def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    characters = {}
    for i in book_text:
        i = i.lower()
        if i not in characters:
            characters[i] = 0
        characters[i] += 1
    return characters

#Create a sorted list of dictionaries, with two keys: character and count
def create_2_keys(characters):
    list = []
    for i in characters:
        list.append({"character": i, "count": characters[i]})
    list.sort(key=lambda x: x["count"], reverse=True)
    return list








