# these are words we want to ignore
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
def delete_stop_words(word_list)
    word_list_copy = word_list[:]
    for word in word_list:
            if word in STOP_WORDS:
                word_list_copy.remove(word)
    return word_list_copy

def delete_stop_words(word_list):
    word_count_copy = word_count[:]
    for word in word_count:
            if word in STOP_WORDS:
                word_count_copy.remove(word)
    return word_count_copy


#OR 

remove_words = [x for x in list_content if x not in STOP_WORDS]

    word_count = [word for word in word_list if word not in STOP_WORDS]