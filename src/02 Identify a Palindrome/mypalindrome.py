

def is_palimdrome(phrase):
    ''' 
      is the phrase a palindrome?
      1. remove non A-Z letters from phrase
      2. lower case the phrase
      3. compare against reversed version

    '''
    oneway = list(''.join(filter(str.isalpha, phrase)).lower())
    otherway = oneway[::-1]
    return oneway == otherway


if __name__ == '__main__':

    print(is_palimdrome('?is this a palindrome?'))
    print(is_palimdrome('Go hang a salami - I\'m a lasagna hog'))
