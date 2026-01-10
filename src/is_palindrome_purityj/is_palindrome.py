def is_palindrome(text: str) -> bool:
    """
    Check whether a given string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters.

    Parameters
    ----------
    text : str
        The input string to check.

    Returns
    -------
    bool
        True if the string is a palindrome, False otherwise.

    Raises
    ------
    TypeError
        If the input is not a string.

    Examples
    --------
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Normalize the string: lowercase and keep only alphanumeric characters
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    return cleaned == cleaned[::-1]
