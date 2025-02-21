def only_the_words(string: str) -> list:
    punctuation_marks=[",", ".", "?", "-", "'", "!", ":", ";"]
    new_string=""
    for index, character in enumerate(string):
        if character in punctuation_marks and (index==0 or index==(len(string)-1)):
            character=""
        elif character in punctuation_marks and (string[index-1]==" " or string[index+1]==" "):
            character=""
        new_string+=character
        
    only_words_list=new_string.split()
    return only_words_list

def main():
    string=input("Enter a string: ")
    only_words_list=only_the_words(string)
    print(f"Only the words in the string: {only_words_list}")

if __name__=="__main__":
    main()