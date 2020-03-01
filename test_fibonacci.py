import fibonacci

def test_get_sum():
    val = fibonacci.get_sum(10)
    assert val == 10

    val = fibonacci.get_sum(100)
    assert val == 188