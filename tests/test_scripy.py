import pytest
from expander.expander import expand_string


def test_stage_1():

    # Stage 1: Basic Range Expansion
    assert expand_string("1-3") == [1, 2, 3]
    assert expand_string("5") == [5]
    assert expand_string("1-2,4") == [1, 2, 4]
    assert expand_string("7,10-12") == [7, 10, 11, 12]


def test_stage_2():

    # Stage 2: Ignore Whitespace and Empty Parts
    assert expand_string(" , 1-3 , ,5 ") == [1, 2, 3, 5]
    assert expand_string("  10 - 12  ,  ") == [10, 11, 12]
    assert expand_string("1-1,, ,2") == [1, 2]


def test_stage_3():

    # Stage 3: Custom Range Delimiters
    assert expand_string("1..3") == [1, 2, 3]
    assert expand_string("4~6") == [4, 5, 6]
    assert expand_string("10 to 12") == [10, 11, 12]
    assert expand_string("1..2, 5~6, 8 to 9") == [1, 2, 5, 6, 8, 9]


def test_stage_4():

    # Stage 4: Handle Reversed or Invalid Ranges Gracefully
    assert expand_string("5-3") == [3, 4, 5]
    assert expand_string("3-3") == [3]
    with pytest.raises(ValueError):
        expand_string("3-a")
    with pytest.raises(ValueError):
        expand_string("a")

def test_stage_5():
    
    # Stage 5: Support Step Values
    assert expand_string("1-10:2") == [1, 3, 5, 7, 9]
    assert expand_string("10-1:3") == [1, 4, 7, 10]
    assert expand_string("3-3:1") == [3]
    with pytest.raises(ValueError):
        expand_string("1-5:x")

def test_stage_6():
    
    # Stage 6: Duplicate and Overlapping Range Handling
    assert expand_string("1-3,2-5,") == [1, 2, 3, 4, 5]
    assert expand_string("3,3,3") == [3]
    assert expand_string("1-2,2-3") == [1, 2, 3]

def test_stage_7():
    
    # Stage 7: Output Format Control
    assert expand_string("1-3", output_format="list") == [1, 2, 3]
    assert expand_string("1-3", output_format="csv") == "1,2,3"
    assert expand_string("1-3", output_format="set") == {1, 2, 3}
    with pytest.raises(ValueError):
        expand_string("1-3", output_format="xml")