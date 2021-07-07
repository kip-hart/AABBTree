import itertools

import pytest

from aabbtree import AABB
from aabbtree import AABBTree


def test_init():
    aabb = AABB([(-2.3, 4.5), (3.6, 8.2)])
    val = 3.1415

    tree = AABBTree()
    assert tree.aabb == AABB()

    tree = AABBTree(aabb, val)
    assert tree.aabb == aabb
    assert tree.value == val
    assert tree.left is None
    assert tree.right is None

    tree2 = AABBTree(aabb, val, tree, tree)
    assert tree2.left == tree
    assert tree2.right == tree


def test_empty_str():
    empty_str = 'AABB: None\nValue: None\nLeft: None\nRight: None'
    assert str(AABBTree()) == empty_str


def test_str_str():
    aabb = standard_aabbs()[0]
    value = 7
    leaf = AABBTree(aabb)
    tree = AABBTree(aabb=aabb, value=value, left=leaf, right=leaf)
    fmt = 'AABB: {}\nValue: {}\nLeft:\n{}\nRight:\n{}'
    assert str(tree) == fmt.format(str(aabb), str(value), leaf.__str__(1),
                                   leaf.__str__(1))


def test_empty_repr():
    assert repr(AABBTree()) == 'AABBTree()'


def test_leaf_repr():
    aabb = standard_aabbs()[0]
    tree = AABBTree()
    tree.add(aabb)
    assert repr(tree) == 'AABBTree(aabb={})'.format(repr(aabb))


def test_str_repr():
    aabb = 'a'
    value = 'v'
    left = 'left'
    right = 'right'
    tree = AABBTree(aabb=aabb, value=value, left=left, right=right)
    fmt = 'AABBTree(aabb={}, value={}, left={}, right={})'
    assert repr(tree) == fmt.format(repr(aabb), repr(value), repr(left),
                                    repr(right))


def test_eq():
    tree = AABBTree()
    tree.add(AABB([(2, 3)]))
    tree.add(AABB([(4, 5)]))
    tree.add(AABB([(-2, 2)]))
    tree2 = AABBTree(tree.aabb)

    assert tree == tree
    assert AABBTree() == AABBTree()
    assert tree != AABBTree()
    assert AABBTree() != tree
    assert AABBTree() != AABB()
    assert tree != tree2
    assert tree2 != tree

    assert not tree != tree
    assert not AABBTree() != AABBTree()
    assert not tree == AABBTree()
    assert not AABBTree() == tree
    assert not AABBTree() == AABB()
    assert not tree == tree2
    assert not tree2 == tree


def test_len():
    tree = AABBTree()
    assert len(tree) == 0

    for i, aabb in enumerate(standard_aabbs()):
        tree.add(aabb)
        assert len(tree) == i + 1


def test_is_leaf():
    assert AABBTree().is_leaf
    assert AABBTree(AABB([(2, 5)])).is_leaf

    tree = AABBTree(AABB([(4, 5)]))
    tree2 = AABBTree()
    tree2.add(tree.aabb)
    tree2.add(tree.aabb)
    assert not tree2.is_leaf


def test_add():
    tree = AABBTree()
    aabb = AABB([(3, 4), (5, 6), (-3, 5)])

    tree.add(aabb)
    tree2 = AABBTree(aabb)
    assert tree == tree2
    assert AABBTree() != tree


def test_add_raises():
    tree = AABBTree()
    with pytest.raises(ValueError):
        for aabb in standard_aabbs():
            tree.add(aabb, method=3.14)


def test_add_merge():
    aabbs = standard_aabbs()
    for indices in itertools.permutations(range(4)):
        tree = AABBTree()
        for i in indices:
            tree.add(aabbs[i])
        aabb_merge(tree)


def aabb_merge(tree):
    if not tree.is_leaf:
        assert tree.aabb == AABB.merge(tree.left.aabb, tree.right.aabb)
        aabb_merge(tree.left)
        aabb_merge(tree.right)


def test_does_overlap():
    aabb5 = AABB([(-3, 3), (-3, 3)])
    aabb6 = AABB([(0, 1), (5, 6)])
    aabb7 = AABB([(6.5, 6.5), (5.5, 5.5)])

    not_tree = AABBTree()
    not_tree.add(aabb6)
    not_tree.add(aabb7)

    for aabb in (aabb5, aabb6, aabb7):
        for m in ('DFS', 'BFS'):
            assert not AABBTree().does_overlap(aabb, method=m)

    aabbs = standard_aabbs()
    for indices in itertools.permutations(range(4)):
        tree = AABBTree()
        alt_tree = AABBTree()
        for i_ind, i in enumerate(indices):
            tree.add(aabbs[i])
            alt_tree.add(aabbs[i_ind])

        for m in ('DFS', 'BFS'):
            assert tree.does_overlap(tree, method=m)
            assert alt_tree.does_overlap(tree, method=m)
            assert tree.does_overlap(alt_tree, method=m)

            assert tree.does_overlap(aabb5, method=m)
            assert not tree.does_overlap(aabb6, method=m)
            assert not tree.does_overlap(aabb7, method=m)

            assert not tree.does_overlap(not_tree, method=m)
            assert not not_tree.does_overlap(tree, method=m)


def test_does_overlap_error():
    method = -1
    aabbs = standard_aabbs()
    tree = standard_tree()
    with pytest.raises(ValueError):
        tree.does_overlap(aabbs[0], method=method)


def test_overlap_aabbs():
    aabbs = standard_aabbs()
    values = ['value 1', 3.14, None, None]

    aabb5 = AABB([(-3, 3.1), (-3, 3)])
    aabb6 = AABB([(0, 1), (5, 6)])
    aabb7 = AABB([(6.5, 6.5), (5.5, 5.5)])

    not_tree = AABBTree()
    not_tree.add(aabb6)
    not_tree.add(aabb7)

    for indices in itertools.permutations(range(4)):
        tree = AABBTree()
        for i in indices:
            tree.add(aabbs[i], values[i])

        for m in ('DFS', 'BFS'):
            assert all([box in tree.overlap_aabbs(tree, method=m)
                        for box in aabbs])
            aabbs5 = tree.overlap_aabbs(aabb5, method=m)
            assert len(aabbs5) == 2
            for aabb in aabbs5:
                assert aabb in aabbs[:2]

            assert tree.overlap_aabbs(aabb6) == []
            assert tree.overlap_aabbs(aabb7) == []

            assert tree.overlap_aabbs(not_tree, method=m) == []
            assert not_tree.overlap_aabbs(tree, method=m) == []

    for m in ('DFS', 'BFS'):
        assert AABBTree(aabb5).overlap_aabbs(aabb7, method=m) == []


def test_overlap_aabbs_error():
    method = -1
    aabbs = standard_aabbs()
    tree = standard_tree()
    with pytest.raises(ValueError):
        tree.overlap_aabbs(aabbs[0], method=method)


def test_overlap_values():
    aabbs = standard_aabbs()
    values = ['value 1', 3.14, None, None]

    aabb5 = AABB([(-3, 3.1), (-3, 3)])
    aabb6 = AABB([(0, 1), (5, 6)])
    aabb7 = AABB([(6.5, 6.5), (5.5, 5.5)])

    for indices in itertools.permutations(range(4)):
        tree = AABBTree()
        for i in indices:
            tree.add(aabbs[i], values[i])

        for m in ('DFS', 'BFS'):
            vals5 = tree.overlap_values(aabb5, method=m)
            assert len(vals5) == 2
            for val in ('value 1', 3.14):
                assert val in vals5

            assert tree.overlap_values(aabb6) == []
            assert tree.overlap_values(aabb7) == []

    for m in ('DFS', 'BFS'):
        assert AABBTree(aabb5).overlap_values(aabb7, method=m) == []


def test_overlap_values_error():
    method = -1
    aabbs = standard_aabbs()
    tree = standard_tree()
    with pytest.raises(ValueError):
        tree.overlap_values(aabbs[0], method=method)


def test_return_the_origin_pass_in_value():
    class Foo:
        pass

    tree = AABBTree()
    value_set = {Foo() for _ in range(10)}

    for value in value_set:
        tree.add(AABB([(0, 1), (0, 1)]), value=value)

    retrieved_value_set = set(tree.overlap_values(AABB([(0, 2), (0, 2)]), unique=False))
    assert retrieved_value_set == value_set


def test_depth():
    assert AABBTree().depth == 0
    assert standard_tree().depth == 2


def test_unique():
    tree = AABBTree()
    aabb1 = AABB([(0, 1)])
    aabb2 = AABB([(0, 1)])
    aabb3 = AABB([(0, 1)])
    tree.add(aabb1, 'box 1')
    tree.add(aabb2, 'box 2')
    vals = tree.overlap_values(aabb3, unique=True)
    assert len(vals) == 1

    vals = tree.overlap_values(aabb3, unique=False)
    assert len(vals) == 2
    assert 'box 1' in vals
    assert 'box 2' in vals


def standard_aabbs():
    aabb1 = AABB([(0, 1), (0, 1)])
    aabb2 = AABB([(3, 4), (0, 1)])
    aabb3 = AABB([(5, 6), (5, 6)])
    aabb4 = AABB([(7, 8), (5, 6)])
    return [aabb1, aabb2, aabb3, aabb4]


def standard_tree():
    aabb1, aabb2, aabb3, aabb4 = standard_aabbs()

    tree = AABBTree()
    tree.add(aabb1, 'value 1')
    tree.add(aabb2, 3.14)
    tree.add(aabb3)
    tree.add(aabb4)
    return tree
