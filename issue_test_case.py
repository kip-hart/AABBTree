from aabbtree import AABB
from aabbtree import AABBTree 
tree = AABBTree()
aabb1 = AABB([(0, 0)])
aabb2 = AABB([(-1, 0)])
tree.add(aabb1, 'box 1')
tree.add(aabb2, 'box 2')
v = tree.overlap_values(aabb2)
print(v)
