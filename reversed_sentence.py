sentence="I am a python test engineer"

def reverse_words_sentence(sentence):

    words=sentence.split(" ")

    new_word=[word[::-1] for word in words]

    new_sentence=" ".join(new_word)

    print(new_sentence)

reverse_words_sentence(sentence)