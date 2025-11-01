def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_char(book_text):
    char_count = {}
    for char in book_text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(items):
    return items["count"]

def sort_char_count(char_count):
    sorted_chars = []
    for char, count in char_count.items():
        sorted_chars.append({"char": char, "count": count})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
    # sorted_chars = []
    # for char, count in char_count.items():
    #     sorted_chars.append({"char": char, "count": count})
    # return sorted(sorted_chars, key=lambda x:x["count"], reverse=True)