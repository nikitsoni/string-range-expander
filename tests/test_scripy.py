from expander.expander import expand_string

def test_cases():
    
    # Stage 1: Basic Range Expansion
    assert expand_string("1-3") == [1, 2, 3]
    assert expand_string("5") == [5]
    assert expand_string("1-2,4") == [1, 2, 4]
    assert expand_string("7,10-12") == [7, 10, 11, 12]