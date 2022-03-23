from my_code import multiplier

def test01():
    EXPECTED_RESULT = 6
    TEST_VALUES = [1,2,3]
    bOK = multiplier(TEST_VALUES) == EXPECTED_RESULT
    try:
        assert(bOK)
        print ("All tests OK")
        return True
    except Exception as e:
        print(str(e))
        return False
    #try-except
#def test01
 
test01()