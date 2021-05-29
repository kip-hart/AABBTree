from aabbtree import AABB
from aabbtree import AABBTree 
tree = AABBTree()
aabb1 = AABB([(0, 0)])
aabb2 = AABB([(-1, 0)])
tree.add(aabb1, 'box 1')
tree.add(aabb2, 'box 2')
# Open Boxes
v = tree.overlap_values(aabb2)
print(v)
# Closed Boxes
v = tree.overlap_values(aabb2, closed=True)
print(v)


print(aabb1.overlaps(aabb2, closed=False))
print(aabb1.overlaps(aabb2, closed=True))
