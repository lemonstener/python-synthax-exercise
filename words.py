def print_upper_words(list):
    ''' Takes each word in a list and capitalizes every letter '''
    # for word in list:
    # print(word.upper()) --
    ''' Print out every word that starts with "e" '''
    # for word in list:
    #     if word[0] == 'e':
    #         print(word.upper())
    ''' Print out all words that start with "h" or "y" '''
    for word in list:
        if word[0] == 'y' or word[0] == 'h':
            print(word.upper())
