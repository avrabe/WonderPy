import unittest
from test.robotTestUtil import RobotTestUtil


class MyTestCase(unittest.TestCase):

    def test_pose(self):
        packet = {}
        robot = RobotTestUtil.make_fake_dash()

        packet['2002'] = {
            'x': 1.2,
            'y': 3.4,
            'degree': 5.6,
        }

        sensor = self._prepare_pose(packet, robot)
        self.assertTrue(sensor.watermark_measured is None)
        self.assertAlmostEquals(sensor.watermark_inferred, 0.0)

        packet['2002'] = {
            'x': 1.2,
            'y': 3.4,
            'degree': 5.6,
            'watermark': 3,
        }

        sensor = self._prepare_pose(packet, robot)
        self.assertAlmostEquals(sensor.watermark_measured, 3)
        self.assertAlmostEquals(sensor.watermark_inferred, 3)

    def _prepare_pose(self, packet, robot):
        robot.sensors.parse(packet)
        sensor = robot.sensors.pose
        self.assertAlmostEquals(sensor.x, -3.4)
        self.assertAlmostEquals(sensor.y, 1.2)
        self.assertAlmostEquals(sensor.degrees, 5.6)
        return sensor


if __name__ == '__main__':
    unittest.main()
