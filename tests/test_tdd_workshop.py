from lib.tdd_workshop import *

def test_sum_numbers(): 
    assert type(sum_numbers(1, 2)) == int

def test_returns_sum_of_arguments():
    assert sum_numbers(1, 2) == 3

def test_returns_an_integer(): 
    assert type(count_letters("dummy string", "c")) == int

def test_single_occurrence_returns_1(): 
    assert count_letters("h", "h") == 1

def test_no_occurence_is_zero(): 
    assert count_letters("r", "h") == 0

def test_empty_string_parameter_returns_0(): 
    assert count_letters("", "h") == 0

def test_two_occurrences_return_2():
    assert count_letters("hh", "h") == 2

def test_upper_case_letters_are_counted():
    assert count_letters("HHHH", "h") == 4

def test_upper_case_character_does_not_break_count(): 
     assert count_letters("hhhh", "H") == 4

def this_is_a_test_case(): 

def this_is_a_second_test_case(): 
    