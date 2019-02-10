.. begin-introduction

AABBTree - Axis-Aligned Bounding Box Trees
==========================================

|s-travis|
|s-cov|
|s-license|

|l-github| `Repository`_
|l-rtd| `Documentation`_
|l-pypi| `PyPI`_

AABBTree is a pure Python implementation of a static d-dimensional
axis aligned bounding box (AABB) tree. It is inspired by
`Introductory Guide to AABB Tree Collision Detection`_
from *Azure From The Trenches*.

.. end-introduction

.. figure:: https://aabbtree.readthedocs.io/en/latest/_images/diagram.png
    :alt: AABB Tree
    :align: center

    Left: An AABB tree, leaves numbered by insertion order.
    Right: The AABBs and their bounding boxes.

.. begin-installation

Installation
============

AABBTree is available through PyPI and can be installed by running::

  pip install aabbtree

To test that the package installed properly, run::

  python -c "import aabbtree"

Alternatively, the package can be installed from source by downloading the
latest release from the `AABBTree repository`_ on GitHub. Extract the source
and, from the top-level directory, run::

  pip install -e .

The ``--user`` flag may be needed, depending on permissions.


Example
========

The following example shows how to build an AABB tree and test for overlap::

  >>> from aabbtree import AABB
  >>> from aabbtree import AABBTree
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


.. begin-documentation

Documentation
=============

Documentation for the project is available at
https://aabbtree.readthedocs.io.

.. end-documentation


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
.. _`Repository` : https://github.com/kip-hart/AABBTree
.. _`Documentation` : https://aabbtree.readthedocs.io
.. _`PyPI` : https://pypi.org/project/aabbtree/
.. _`Introductory Guide to AABB Tree Collision Detection` : https://www.azurefromthetrenches.com/introductory-guide-to-aabb-tree-collision-detection/
.. |s-license| image:: https://img.shields.io/pypi/l/aabbtree.svg
    :target: https://github.com/kip-hart/AABBTree/blob/master/LICENSE.rst
    :alt: License
.. |s-docs| image:: https://readthedocs.org/projects/aabbtree/badge/?version=latest
    :target: https://aabbtree.readthedocs.io
    :alt: Documentation Status
.. |s-travis| image:: https://travis-ci.org/kip-hart/AABBTree.svg?branch=master
    :target: https://travis-ci.org/kip-hart/AABBTree
    :alt: Travis CI
.. |s-cov| image:: https://coveralls.io/repos/github/kip-hart/AABBTree/badge.svg?branch=master
    :target: https://coveralls.io/github/kip-hart/AABBTree?branch=master
    :alt: Coverage
.. |s-pver| image:: https://img.shields.io/pypi/v/aabbtree.svg
    :target: https://pypi.org/project/aabbtree/
    :alt: PyPI

.. |l-github| image:: https://api.iconify.design/octicon:mark-github.svg?color=black0&inline=true&height=16
    :target: https://github.com/kip-hart/AABBTree
    :alt: GitHub

.. |l-rtd| image:: https://api.iconify.design/simple-icons:readthedocs.svg?color=black&inline=true&height=16
    :target: https://aabbtree.readthedocs.io
    :alt: ReadTheDocs

.. |l-pypi| image:: https://api.iconify.design/mdi:cube-outline.svg?color=black&inline=true&height=16
    :target: https://pypi.org/project/aabbtree/
    :alt: PyPI
