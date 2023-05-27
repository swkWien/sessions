"""
Word Count Kata and using Exceptions for Control Flow
"""
import pytest


class ControlFlow(Exception):
    pass


class EmptyText(ControlFlow):
    pass


class BlankFound(ControlFlow):
    pass


class CountComplete(ControlFlow):
    pass  # TODO: use instead of IndexError and provide count as argument in exception


def wordcount(text):
    text = text.replace("  ", " ")
    try:
        raise_on(text == "", EmptyText)  # looks like event
        return count_blanks(text) + 1
    except EmptyText:
        return 0


def raise_on(condition, exception):
    try:
        1 / int(not condition)  # condition and 1/0
    except ZeroDivisionError:
        raise exception


def count_blanks(text):
    count_for_some_time = call_twice(call_twice(call_twice(count_per_character)))
    _, count, _ = count_for_some_time(text, 0, 0)
    return count


def call_twice(fun):
    def new_fun(*args):
        result_from_first_call = fun(*args)
        result_from_second_call = fun(*result_from_first_call)

        return result_from_second_call

    return new_fun


def count_per_character(text, count, index):
    try:
        character = text[index]
        raise_on(character == " ", BlankFound)
    except BlankFound:
        count = count + 1
    except IndexError:  # deal with out of range
        pass
    index = index + 1
    return text, count, index


def test_wordcount_with_empty_text():
    assert wordcount("") == 0


def test_wordcount_with_single_character():
    assert wordcount("a") == 1


def test_wordcount_with_two_words():
    assert wordcount("a a") == 2


def test_wordcount_with_two_words_separated_by_two_whitespaces():
    assert wordcount("a  a") == 2


def test_wordcount_with_one_word_of_length_five():
    assert wordcount("abcde") == 1


def test_wordcount_with_one_long_word_and_one_short_word():
    assert wordcount("abcde f") == 2


def test_call_twice():
    fun_to_call = lambda a, b: (a + b, b)  # TODO replace by power of two
    assert call_twice(fun_to_call)(1, 3) == (7, 3)
    assert call_twice(call_twice(fun_to_call))(1, 3) == (13, 3)
    assert call_twice(call_twice(call_twice(fun_to_call)))(1, 3) == (25, 3)
