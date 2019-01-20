from aabb import AABB, AABBTree


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


def test_repr():
    aabb1 = AABB([(0, 1), (0, 1)])
    aabb2 = AABB([(3, 4), (0, 1)])
    aabb3 = AABB([(5, 6), (5, 6)])
    aabb4 = AABB([(7, 8), (5, 6)])

    tree = AABBTree()
    tree.add(aabb1, 'x')
    tree.add(aabb2, 'y')
    tree.add(aabb3, 3.14)
    tree.add(aabb4)

    assert tree == eval(repr(tree))
    assert AABBTree() == eval(repr(AABBTree()))


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


def test_add_merge():
    aabb1 = AABB([(0, 1), (0, 1)])
    aabb2 = AABB([(3, 4), (0, 1)])
    aabb3 = AABB([(5, 6), (5, 6)])
    aabb4 = AABB([(7, 8), (5, 6)])

    tree = AABBTree()
    tree.add(aabb1)
    tree.add(aabb2)
    tree.add(aabb3)
    tree.add(aabb4)

    aabb_merge(tree)


def aabb_merge(tree):
    if not tree.is_leaf:
        assert tree.aabb == AABB.merge(tree.left.aabb, tree.right.aabb)
        aabb_merge(tree.left)
        aabb_merge(tree.right)


def test_does_overlap():
    aabb1 = AABB([(0, 1), (0, 1)])
    aabb2 = AABB([(3, 4), (0, 1)])
    aabb3 = AABB([(5, 6), (5, 6)])
    aabb4 = AABB([(7, 8), (5, 6)])

    aabb5 = AABB([(-3, 3), (-3, 3)])
    aabb6 = AABB([(0, 1), (5, 6)])

    tree = AABBTree()
    tree.add(aabb1)
    tree.add(aabb2)
    tree.add(aabb3)
    tree.add(aabb4)

    assert tree.does_overlap(aabb5)
    assert not tree.does_overlap(aabb6)


def test_overlap_values():
    aabb1 = AABB([(0, 1), (0, 1)])
    aabb2 = AABB([(3, 4), (0, 1)])
    aabb3 = AABB([(5, 6), (5, 6)])
    aabb4 = AABB([(7, 8), (5, 6)])

    aabb5 = AABB([(-3, 3.1), (-3, 3)])
    aabb6 = AABB([(0, 1), (5, 6)])

    tree = AABBTree()
    tree.add(aabb1, 'value 1')
    tree.add(aabb2, 3.14)
    tree.add(aabb3)
    tree.add(aabb4)

    print(tree)

    vals5 = tree.overlap_values(aabb5)
    assert len(vals5) == 2
    for val in ('value 1', 3.14):
        assert val in vals5

    assert tree.overlap_values(aabb6) == []
