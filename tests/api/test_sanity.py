#pytest - test files ==  functions prefixing "test"
#command - pytest "path" -v
#includes "assert" for returning results

def test_sanity():
    assert 1+1 == 2;


def test_string_check():
    assert "hello".upper() == "HELLO"

    
