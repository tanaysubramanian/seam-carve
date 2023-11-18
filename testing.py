import pytest

from edits import edit_distance_bwd, edit_distance_fwd
from seamcarve import SeamCarve

def test_seamcarve():
    # original 5x5 spreadsheet
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    expected_seam = [2, 1, 1, 2, 3]

    my_sc = SeamCarve(image_matrix = test_image)

    importance_vals = my_sc.calculate_importance_values()
    calculated_seam = my_sc.find_least_important_seam(importance_vals)

    assert expected_seam == calculated_seam

    assert my_sc.argmin([5]) == 0
    assert my_sc.argmin([1,2,3,4]) == 0
    assert my_sc.argmin([3, 8, 17, 100, 2]) == 4
    assert my_sc.argmin([500, 200, 4, 1, 900]) == 3
    assert my_sc.argmin([5, -3, -2, 7, 9, -1, -3]) == 1
    assert my_sc.argmin([2, 2, 1, 1, 1]) == 2

    # modified 5x5 spreadsheet - checkerboard
    test_image1 = [[[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], 
        [255, 255, 255]], [[0, 0, 0], [255, 255, 255], [0, 0, 0], 
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [0, 0, 0], 
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0], 
        [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], 
        [255, 255, 255]]]
    expected_seam1 = [0, 0, 0, 0, 0]

    my_sc1 = SeamCarve(image_matrix = test_image1)

    importance_vals1 = my_sc1.calculate_importance_values()
    calculated_seam1 = my_sc1.find_least_important_seam(importance_vals1)

    assert expected_seam1 == calculated_seam1

    # modified 5x5 spreadsheet - all black
    test_image2 = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], 
        [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], 
        [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], 
        [0, 0, 0], [0, 0, 0]]]
    expected_seam2 = [0, 0, 0, 0, 0]

    my_sc2 = SeamCarve(image_matrix = test_image2)

    importance_vals2 = my_sc2.calculate_importance_values()
    calculated_seam2 = my_sc2.find_least_important_seam(importance_vals2)

    assert expected_seam2 == calculated_seam2

    # modified 5x5 spreadsheet - gradually getting darker closer to center for
    # top half and random shades on bottom
    test_image3 = [[[250, 250, 250], [250, 250, 250], [250, 250, 250], 
        [250, 250, 250], [250, 250, 250]], [[250, 250, 250], [100, 100, 100], 
        [100, 100, 100], [100, 100, 100], [250, 250, 250]], [[250, 250, 250], 
        [100, 100, 100], [10, 10, 10], [100, 100, 100], [250, 250, 250]], 
        [[130, 130, 130], [50, 50, 50], [100, 100, 100], [90, 90, 90], 
        [49, 49, 49]], [[66, 66, 66], [200, 200, 200], [120, 120, 120], 
        [250, 250, 250], [200, 200, 200]]]
    expected_seam3 = [4, 4, 3, 2, 2]

    my_sc3 = SeamCarve(image_matrix = test_image3)

    importance_vals3 = my_sc3.calculate_importance_values()
    calculated_seam3 = my_sc3.find_least_important_seam(importance_vals3)

    assert expected_seam3 == calculated_seam3

    # modified 8x8 spreadsheet - dividing shades randomly
    test_image4 = [[[110, 110, 110], [0, 0, 0], [73, 73, 73], [180, 180, 180], 
    [240, 240, 240], [0, 0, 0], [0, 0, 0], [240, 240, 240]], [[0, 0, 0], 
    [200, 200, 200], [0, 0, 0], [10, 10, 10], [200, 200, 200], [10, 10, 10], 
    [200, 200, 200], [0, 0, 0]], [[180, 180, 180], [0, 0, 0], [240, 240, 240], 
    [0, 0, 0], [110, 110, 110], [240, 240, 240], [180, 180, 180], [0, 0, 0]], 
    [[73, 73, 73], [200, 200, 200], [200, 200, 200], [73, 73, 73], [0, 0, 0], 
    [200, 200, 200], [0, 0, 0], [110, 110, 110]], [[0, 0, 0], [0, 0, 0], 
    [110, 110, 110], [180, 180, 180], [200, 200, 200], [110, 110, 110], 
    [240, 240, 240], [0, 0, 0]], [[0, 0, 0], [200, 200, 200], [240, 240, 240], 
    [0, 0, 0], [0, 0, 0], [0, 0, 0], [73, 73, 73], [0, 0, 0]], [[0, 0, 0], 
    [180, 180, 180], [73, 73, 73], [200, 200, 200], [200, 200, 200], 
    [110, 110, 110], [180, 180, 180], [200, 200, 200]], [[240, 240, 240], 
    [110, 110, 110], [0, 0, 0], [200, 200, 200], [0, 0, 0], [0, 0, 0], 
    [240, 240, 240], [73, 73, 73]]]
    expected_seam4 = [2, 3, 3, 2, 1, 0, 1, 1]

    my_sc4 = SeamCarve(image_matrix = test_image4)

    importance_vals4 = my_sc4.calculate_importance_values()
    calculated_seam4 = my_sc4.find_least_important_seam(importance_vals4)

    assert expected_seam4 == calculated_seam4

    # modified 8x8 spreadsheet - dividing shades diagonally
    test_image5 = [[[40, 40, 40], [80, 80, 80], [13, 13, 13], [200, 200, 200], 
    [90, 90, 90], [110, 110, 110], [25, 25, 25], [250, 250, 250]], 
    [[80, 80, 80], [13, 13, 13], [200, 200, 200], [90, 90, 90], [110, 110, 110],
    [25, 25, 25], [250, 250, 250], [30, 30, 30]], [[13, 13, 13], [200, 200, 200]
    , [90, 90, 90], [110, 110, 110], [25, 25, 25], [250, 250, 250], [30, 30, 30]
    , [130, 130, 130]], [[200, 200, 200], [90, 90, 90], [110, 110, 110], 
    [25, 25, 25], [250, 250, 250], [30, 30, 30], [130, 130, 130], 
    [200, 200, 200]], [[90, 90, 90], [110, 110, 110], [25, 25, 25], 
    [250, 250, 250], [30, 30, 30], [130, 130, 130], [200, 200, 200], 
    [73, 73, 73]], [[110, 110, 110], [25, 25, 25], [250, 250, 250], [30, 30, 30]
    , [130, 130, 130], [200, 200, 200], [73, 73, 73], [220, 220, 220]], 
    [[25, 25, 25], [250, 250, 250], [30, 30, 30], [130, 130, 130], 
    [200, 200, 200], [73, 73, 73], [220, 220, 220], [5, 5, 5]], [[250, 250, 250]
    , [30, 30, 30], [130, 130, 130], [200, 200, 200], [73, 73, 73], 
    [220, 220, 220], [5, 5, 5], [90, 90, 90]]]
    expected_seam5 = [4, 4, 3, 2, 1, 0, 1, 2]

    my_sc5 = SeamCarve(image_matrix = test_image5)

    importance_vals5 = my_sc5.calculate_importance_values()
    calculated_seam5 = my_sc5.find_least_important_seam(importance_vals5)

    assert expected_seam5 == calculated_seam5
