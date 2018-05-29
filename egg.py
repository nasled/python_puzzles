import unittest

def highest_floor(total_floors, highest_floor = 1):
    total_steps = 0
    runner_offset = round(total_floors / 2)

    for floor in range(1, total_floors+1):
        # first egg, or odd floors in building
        if highest_floor == floor or floor == runner_offset:
            total_steps += floor * 2
            break

        # second egg
        runner_floor = runner_offset + floor
        if highest_floor == runner_floor:
            total_steps += runner_floor * 2
            break

        total_steps += runner_floor * 2

    return total_steps

class TestHighestFloorIsBellowTheMax(unittest.TestCase):
    def test_worst(self):
        self.assertLess(highest_floor(0, 0), 1)
        self.assertLess(highest_floor(1, 0), 3)
        self.assertLess(highest_floor(2, 0), 5)
        self.assertLess(highest_floor(11, 0), 103)
        self.assertLess(highest_floor(111, 0), 9353)
        self.assertLess(highest_floor(222, 0), 36853)
        self.assertLess(highest_floor(333, 0), 82503)
        self.assertLess(highest_floor(444, 0), 147631)

    def test_third(self):
        self.assertLess(highest_floor(0, 3), 1)
        self.assertLess(highest_floor(10, 3), 33)
        self.assertLess(highest_floor(11, 3), 37)

unittest.main()