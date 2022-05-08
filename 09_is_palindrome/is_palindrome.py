def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    clean_phrase = phrase.lower().replace(" ","")
    phrase_list = list(clean_phrase)
    phrase_list.reverse()
    result = ""
    for char in phrase_list:
        result += char
    
    return (result == clean_phrase)



