
"""Replaces a character in all string of a list"""
def replaceList (list_of_strings:list, old:str, new:str) -> list:
    for i in range(len(list_of_strings)):
        list_of_strings[i] = list_of_strings[i].replace(old, new)
    return list_of_strings

"""Fetches each line of a text file in a list"""
def fetchContentList (filename) -> list:
    lines = []
    with open(f'./messages/{filename}', 'r') as file:
        lines = file.readlines()
    return replaceList(lines, '\n', '')

"""Fetches the contents of a text file"""
def fetchContent (filename) -> str:
    filename = f'./messages/{filename}'
    f = open(filename, 'r')
    return f.read(), f