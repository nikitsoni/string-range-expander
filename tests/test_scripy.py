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