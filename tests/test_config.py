def test_something():  #for test case name must start with test
    a=2
    b=2
    assert a==b

import pytest

class NotInRange(Exception):
    def __init__(self,message="Value not in Range"):
        self.message = message
        super().__init__(self.message)

def test_genric():
    a=5
    with pytest.raises(NotInRange):
        if a not in range(10,15):
            raise NotInRange
