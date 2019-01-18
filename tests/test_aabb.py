from aabb import AABB


def test_init():
    box = [(0, 1), (0, 1)]
    aabb = AABB(box)

    assert len(box) == len(aabb)

    for lims_box, lims_aabb in zip(box, aabb):
        assert lims_box[0] == lims_aabb[0]
        assert lims_box[1] == lims_aabb[1]
