import pytest

from aabbtree import AABB


def test_init():
    box = [(0, 1), (0, 1)]
    aabb = AABB(box)

    assert len(box) == len(aabb)

    for lims_box, lims_aabb in zip(box, aabb):
        assert lims_box[0] == lims_aabb[0]
        assert lims_box[1] == lims_aabb[1]

    assert AABB().limits is None

    box2 = [(-4, -10)]
    box3 = [(1, 2, 3)]
    for bad_box in (box2, box3):
        with pytest.raises(ValueError):
            AABB(bad_box)


def test_eq():
    limits1 = [(-2, 3), (1, 2.3)]
    limits2 = [(-2, 3), (2, 2.3)]

    aabb1 = AABB(limits1)
    aabb2 = AABB(limits2)
    aabb3 = AABB(limits2)

    assert aabb1 == aabb1
    assert aabb1 != aabb2
    assert aabb2 != aabb1
    assert aabb2 == aabb3

    assert aabb1 != limits1
    assert AABB([(2, 3)]) != aabb1
    assert AABB() == AABB()
    assert aabb1 != AABB()
    assert AABB() != aabb1

    assert not aabb1 != aabb1
    assert not aabb1 == aabb2
    assert not aabb2 == aabb1
    assert not aabb2 != aabb3

    assert not aabb1 == limits1
    assert not AABB([(2, 3)]) == aabb1
    assert not AABB() != AABB()
    assert not aabb1 == AABB()
    assert not AABB() == aabb1


def test_str():
    limits = [(2, 3), (-20, 24), (2.3, 6.71)]
    assert str(limits) == str(AABB(limits))


def test_repr():
    line = [(2, 3)]
    aabb = AABB(line)
    assert repr(aabb) == 'AABB(' + repr(line) + ')'


def test_merge():
    aabb1 = AABB([(0, 1)])
    aabb2 = AABB([(-1, 2)])
    assert aabb2 == AABB.merge(aabb1, aabb2)

    aabb3 = AABB([(0.5, 3)])
    assert AABB([(0, 3)]) == AABB.merge(aabb1, aabb3)

    assert aabb1 == AABB.merge(aabb1, AABB())
    assert aabb2 == AABB.merge(AABB(), aabb2)
    assert AABB() == AABB.merge(AABB(), AABB())

    aabb3 = AABB([(-1, 0), (2, 3), (1, 5)])
    with pytest.raises(ValueError):
        AABB.merge(aabb1, aabb3)


def test_perimeter():
    # 1D
    assert AABB([(0, 1)]).perimeter == 0

    # 2D
    len1 = 4
    len2 = 5.2
    p_exp = 2 * (len1 + len2)
    assert AABB([(0, len1), (-2, -2 + len2)]).perimeter == p_exp

    # 3D
    assert AABB([(-3, -2), (4, 5), (0, 1)]).perimeter == 6
    assert AABB([(2, 2), (3, 3), (-1, -1)]).perimeter == 0
    assert AABB([(4, 4), (0, 1), (0, 1)]).perimeter == 2


def test_overlaps():
    aabb1 = AABB([(0, 10), (0, 10)])
    aabb2 = AABB([(-5, 5), (-6, 3)])
    aabb3 = AABB([(10, 12), (5, 6)])

    assert aabb1.overlaps(aabb2)
    assert aabb2.overlaps(aabb1)
    assert not aabb3.overlaps(aabb2)
    assert not aabb2.overlaps(aabb3)


def test_overlaps_closed():
    aabb1 = AABB([(0, 0)])
    aabb2 = AABB([(-1, 0)])
    aabb3 = AABB([(1, 2)])
    aabb4 = AABB([(-9, -8)])

    assert aabb1.overlaps(aabb2, True)
    assert aabb2.overlaps(aabb1, True)
    assert not aabb1.overlaps(aabb3, True)
    assert not aabb2.overlaps(aabb3, True)
    assert not aabb1.overlaps(aabb4, True)
    assert not aabb2.overlaps(aabb4, True)
    assert not aabb1.overlaps(AABB(), True)


def test_corners():
    lims = [(0, 10), (5, 10)]
    aabb_corners = [
        [lims[0][0], lims[1][0]],
        [lims[0][1], lims[1][0]],
        [lims[0][0], lims[1][1]],
        [lims[0][1], lims[1][1]]
    ]

    out_corners = AABB(lims).corners
    for c in aabb_corners:
        assert c in out_corners

    for c in out_corners:
        assert c in aabb_corners


def test_next():
    box = [(0, 1), (0, 1)]
    aabb = AABB(box)
    aabb._i = 2 + 1
    with pytest.raises(StopIteration):
        aabb.__next__()
