



def stutter(word: str) -> str:
    """
    Return a string with the first two letters of the word repeated twice, followed by the word followed by a question mark.
    Parameters:
    word: str -> The word to be stuttered.
    """
    if not isinstance(word, str):
        raise TypeError("Only strings are allowed")
    
    return f"{word[0:2]}... {word[0:2]}... {word}?"




print(stutter("Hola mundo"))



