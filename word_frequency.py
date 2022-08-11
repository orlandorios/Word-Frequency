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
        print(count_words(text_document.lower().translate(str.maketrans('', '', string.punctuation))))
        # using method function *.lower* to change text to lowercase
        # using method .translate method function to replace any character. 
        # str.maketrans returns a mapping table
        # quotations are left empty to signal when string occurs a punctuation to leave empty
    
# create a new function to convert a string into a dictonary
# taking a word and mapping to a number (number of occurences in the original string)
def count_words(text):
    word_count = dict() #leave dictionary object empty since pulling information from text file
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
    return word_count
#function to count words in a string
#in dictionaries, you can not have 2 keys with the same name

    pass

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
