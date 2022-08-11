# these are words we want to ignore
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file_path):   
    """Read in `file` and print out the frequency of words in that file."""
    with file_path.open() as text_document_file:
        #calling a function to read the contents of a file to return 
        # as a string
        #file_path.open gives access to file defined at file_path
        #file_path is a path object
        #text_document_file is a file handle
        text_document = text_document_file.read()
        #text_document primative data type is string (text characters)
        print(format_word_count(remove_stop_words(count_words(text_document.lower().translate(str.maketrans('', '', string.punctuation))),STOP_WORDS)))
        # using method function *.lower* to change text to lowercase
        # using method .translate method function to replace any character
        # str.maketrans returns a mapping table
        # quotations are left empty to signal when string occurs a punctuation to leave
    
# create a new function to convert a string into a dictonary
# taking a word and mapping to a number (number of occurences in the original string)
def count_words(text):
    word_count = dict() #leave dictionary object empty since pulling information from text file
    #in dictionaries, you can not have 2 keys with the same name
    #dictionaries purpose is to pull a list of keys and assign a value
    # text = "insert text here" **line of code not needed due to formal parameter (text) has already been defined**
    word_list = text.split()
    # this is not a free function, it is a method which is a function called differently
    # text.split function value is returning a list *which is why variable named word_list*
    for word in word_list:
        if word in word_count:
            # if word already exists in dictionary, increment value by 1
            word_count[word] += 1
            # key is accessing dictionary and adding increment value of 1 to exisiting count
        else:
            # if word does not exists in dictionary, needs to be added to the dictionary with initial value of 1
            word_count[word] = 1
            # key is getting access to element of the dictionary 
    # word_count = list(map(list,word_count.items()))
    # converting the dictionary into list
    # word_count = word_count.items()
    
    return word_count

def remove_stop_words(word_count, STOP_WORDS):
    # create function to copy dictionary with stop words removed
    redacted_copy = dict()
    # create empty dictionary to populate copy of previous dictionary
    for word, count, in word_count.items():
        # key always comes first before the value
        # destruture tuple to access the key and value 
        if word not in STOP_WORDS:
            # only copy word and count if not included in copy array
            redacted_copy[word] = count        
    
    return redacted_copy

def format_word_count(word_count):
    # create new function to format dictionary to give full control how the dictionary looks when printed out
    # first step format dictionary into a string
    formatted_list = ""
    # using class constructor to convert dictionary back into string
    for word, count, in word_count.items():
        # key always comes first before the value
        # destruture tuple to access the key and value 
        formatted_list += ('\n' + word + ' | ' + str(count) + ' ' + ('*' * count))
        #concatenate into list, with the key, then turn the integer value into a string
        
    return formatted_list
#     # if function doesn't have a value to return, it will return none


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file_path = Path(args.file)
    if file_path.is_file():
        print_word_freq(file_path)
    else:
        print(f"{file_path} does not exist!")
        exit(1)
        



# word_count_map = {
#     #taking a word and mapping to a number (number of occurences in the original string)
# }
