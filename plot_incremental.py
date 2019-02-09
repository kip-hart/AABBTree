import os

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import aabbtree


def plot_contents(tree, level=0):
    if tree.is_leaf:
        color = 'k'
        ls = '-'
    else:
        color = 'C' + str(level % 10)
        ls = ':'

    xlims, ylims = tree.aabb.limits
    xy = [xlims[0], ylims[0]]
    w = xlims[1] - xlims[0]
    h = ylims[1] - ylims[0]
    rec = Rectangle(xy, w, h, linestyle=ls, facecolor='none', edgecolor=color)
    plt.gca().add_patch(rec)

    if tree.is_leaf:
        leaf_id = str(tree.value)
        xy = [0.5 * (lims[0] + lims[1]) for lims in tree.aabb]
        plt.text(xy[0], xy[1], leaf_id, ha='center', va='center')

    else:
        plot_contents(tree.left, level + 1)
        plot_contents(tree.right, level + 1)


def plot_tree(tree, level=0, center=(-55, 5)):
    if tree.is_leaf:
        color = 'k'
        ls = '-'
    else:
        color = 'C' + str(level % 10)
        ls = ':'

    w = 3
    h = 3
    xy = [center[0] - 0.5 * w, center[1] - 0.5 * h]
    rec = Rectangle(xy, w, h, linestyle=ls, facecolor='none', edgecolor=color)
    plt.gca().add_patch(rec)

    if tree.is_leaf:
        leaf_id = str(tree.value)
        plt.text(center[0], center[1], leaf_id, ha='center', va='center')

    if not tree.is_leaf:
        dx = 30 / 2 ** level
        cx = center[0] + 0.5 * dx
        cy = center[1] - 6
        plt.plot([center[0], cx], [xy[1], cy + 0.5 * h], 'k', lw=0.5)
        plot_tree(tree.right, level + 1, [cx, cy])

        cx -= dx
        plt.plot([center[0], cx], [xy[1], cy + 0.5 * h], 'k', lw=0.5)
        plot_tree(tree.left, level + 1, [cx, cy])


def main():
    # Cross shapes
    cross_horiz_left = aabbtree.AABB([(-6, 1), (-1, 2)])
    cross_vert_left = aabbtree.AABB([(-1, 1), (-15, 5)])
    cross_horiz_right = aabbtree.AABB([(3, 10), (-2, 1)])
    cross_vert_right = aabbtree.AABB([(3, 5), (-15, 5)])

    # Box sets
    box_1 = aabbtree.AABB([(-21, -18), (-21, -18)])
    box_2 = aabbtree.AABB([(-17, -14), (-21, -18)])
    box_3 = aabbtree.AABB([(-16, -13), (-16, -13)])
    box_4 = aabbtree.AABB([(-12, -9), (-16, -13)])

    # Random boxes
    rand_1 = aabbtree.AABB([(-15, -13), (-2, 2)])

    # Build tree
    tree = aabbtree.AABBTree()
    aabbs = [box_3, cross_vert_right, box_1, cross_horiz_left, box_4,
             rand_1, cross_vert_left, box_2, cross_horiz_right]
    for i, aabb in enumerate(aabbs):
        tree.add(aabb, i + 1)

    # Set up figure
    plt.clf()
    plt.close('all')
    fig = plt.figure()
    ax = plt.axes()
    ax.set_axis_off()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    fig.add_axes(ax)

    # Plot tree contents
    plot_contents(tree)

    # Plot tree
    plot_tree(tree)

    # Format axes
    plt.axis('square')
    plt.xlim([-85, 11])
    plt.ylim([-22, 7])

    # Save figure
    docs_path = os.path.join(os.path.dirname(__file__), 'docs')
    fig_filename = os.path.join(docs_path, 'source', '_static', 'diagram.png')
    plt.savefig(fig_filename, dpi=300, bbox_inches='tight', pad_inches=0,
                transparent=True)


if __name__ == '__main__':
    main()
