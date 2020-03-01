import sum_multiples

def test_get_sum():
    val = sum_multiples.get_sum(10)
    assert val == 23

    val = sum_multiples.get_sum(100)
    assert val == 2318

