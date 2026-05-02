def longest_word(word_list):
    max_word=""
    for word in word_list:
        if len(word)>len(max_word):
            max_word=word
    return max_word
word_list=input("Enter the words seperated with spaces: ").split()
max_word=longest_word(word_list)
print(f"The longest word is {max_word} and length is {len(max_word)}")
