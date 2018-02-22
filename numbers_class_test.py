import pytest
import numbers_class


def test_find_max_diff():
    from math import isclose

    list_1_diff = numbers_class.numberInfo((1, 4, 10))
    list_2_diff = numbers_class.numberInfo((0, -8, -4, 0, 4, 11))
    list_3_diff = numbers_class.numberInfo((7, 7, 7, 7, 7))
    list_4_diff = numbers_class.numberInfo((0, 0.1, 0.205, 0.3))
    list_5_diff = numbers_class.numberInfo((-7, 0, -7))

    assert list_1_diff.maxDiff == 6
    assert list_2_diff.maxDiff == -8
    assert list_3_diff.maxDiff == 0
    assert isclose(list_4_diff.maxDiff, 0.105, abs_tol=10e-9)
    assert list_5_diff.maxDiff == [-7, 7]


def test_max_diff_exceptions(capsys):
    list1 = numbers_class.numberInfo([])
    out1, err1 = capsys.readouterr()
    list2 = numbers_class.numberInfo([1])
    out2, err2 = capsys.readouterr()
    list3 = numbers_class.numberInfo([0, 1, 2, 'Hello'])
    out3, err3 = capsys.readouterr()

    assert list1.maxDiff is None
    assert list2.maxDiff is None
    assert list3.maxDiff is None
    assert out1 == 'Numerical list must be at least of length 2\n'
    assert out2 == 'Numerical list must be at least of length 2\n'
    assert out3 == 'Only numerical lists accepted\n'


def test_sum_list(capsys):
    sum_1 = numbers_class.numberInfo([5])
    sum_2 = numbers_class.numberInfo([2, 7])
    sum_3 = numbers_class.numberInfo([4, 8.5, 1.2])
    sum_4 = numbers_class.numberInfo([-4, 6, -2])
    sum_5 = numbers_class.numberInfo([0, 0.6, -1.9, 12.3])

    # exceptions
    sum_6 = numbers_class.numberInfo([0, 5, 'Heya'])
    out6, err6 = capsys.readouterr()
    sum_7 = numbers_class.numberInfo([])
    out7, err7 = capsys.readouterr()
    sum_8 = numbers_class.numberInfo([5, float('inf')])
    out8, err8 = capsys.readouterr()

    assert sum_1.sumList == 5
    assert sum_2.sumList == 9
    assert sum_3.sumList == 13.7
    assert sum_4.sumList == 0
    assert sum_5.sumList == 11

    assert sum_6.sumList is None
    assert sum_7.sumList is None
    assert sum_8.sumList is None
    # 6 raises TypeError, 7 raises TypeError, 8 raises ValueError
    assert out6 == 'Only numerical lists are accepted\n'
    assert out7 == 'Only numerical lists are accepted\n'
    assert out8 == 'Input contains inappropriate value\n'


def test_minmax():
    t1 = numbers_class.numberInfo([1, 5, 3, 9, 5, 6])
    t2 = numbers_class.numberInfo([1.5, 3, 4, 912, 10.4, 0, 0])
    t3 = numbers_class.numberInfo([1.239, 1.2459, 5.6, -5])

    assert t1.minMax == (1, 9)
    assert t2.minMax == (0, 912)
    assert t3.minMax == (-5, 5.6)


def test_minmax_exceptions(capsys):
    t1 = numbers_class.numberInfo([])
    out1, err1 = capsys.readouterr()
    t2 = numbers_class.numberInfo(['One', 'Two', 'Three'])
    out2, err2 = capsys.readouterr()

    assert t1.minMax is None
    assert t2.minMax is None
    assert out1 == 'Numerical list must be at least of length 1\n'
    assert out2 == 'Only numerical lists accepted\n'
