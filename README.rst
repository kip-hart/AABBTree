AABBTree
========

AABBTree is a pure Python implementation of a static d-dimensional
axis aligned bounding box (AABB) tree. It is heavily based on
`Introductory Guide to AABB Tree Collision Dectection`_
from *Azure From The Trenches*.


Installation
============

AABBTree is available through PyPI and can be installed by running::

  pip install aabb

To test that the package installed properly, run::

  python -c "import aabb"

Alternatively, the package can be installed from source by downloading the
latest release from the `AABBTree repository`_ on GitHub. Extract the source
and, from the top-level directory, run::

  pip install -e .

The ``--user`` flag may be needed, depending on permissions.


Example
========

The following example shows how to build an AABB tree and test for overlap::

  >>> from aabb import AABB, AABBTree
  >>> tree = AABBTree()
  >>> aabb1 = AABB([(0, 0), (0, 0)])
  >>> aabb2 = AABB([(-1, 1), (-1, 1)])
  >>> aabb3 = AABB([(4, 5), (2, 3)])
  >>> tree.add(aabb1, 'box 1')
  >>> tree.does_overlap(aabb2)
  True
  >>> tree.overlap_values(aabb2)
  ['box 1']
  >>> tree.does_overlap(aabb3)
  False
  >>> tree.add(aabb3)
  >>> print(tree)
  AABB: [(0, 5), (0, 3)]
  Value: None
  Left:
    AABB: [(0, 0), (0, 0)]
    Value: box 1
    Left: None
    Right: None
  Right:
    AABB: [(4, 5), (2, 3)]
    Value: None
    Left: None
    Right: None


Documentation
=============

Documentation for the project will be available online soon.


Contributing
============

Contributions to the project are welcome.
Please visit the `AABBTree repository`_ to clone the source files,
create a pull request, and submit issues.


License and Copyright Notice
============================

Copyright |copy| 2019, Georgia Tech Research Corporation

AABBTree is open source and freely available under the terms of
the MIT license.


.. |copy| unicode:: 0xA9 .. copyright sign
.. _`AABBTree repository` : https://github.com/kip-hart/AABBTree
.. _`Introductory Guide to AABB Tree Collision Dectection` : https://www.azurefromthetrenches.com/introductory-guide-to-aabb-tree-collision-detection/
