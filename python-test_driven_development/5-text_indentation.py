#!/usr/bin/python3
''' Write a function that prints a text with 2 new lines after each of thes'''


def text_indentation(text):
    ''' text  identation  '''
    validate_text(text)
    
    formatted_text = format_text(text)
    print(formatted_text, end='')


def validate_text(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')


def format_text(text):
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    text = text.replace('.', '.\n\n')
    text = text.replace('\n ', '\n')
    
    if text.endswith('\n'):
        text = text[:-1]
    
    return text
