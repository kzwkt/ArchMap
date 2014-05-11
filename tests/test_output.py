import unittest

import archmap


class OutputTestCase(unittest.TestCase):
    """These tests compare the output of ``make_geojson()``, ``make_kml()``  and ``make csv()``
    with pre-generated versions that have been checked manually, these *sample* files were
    generated by runing ``archmap.py`` on the handmade users file ``sample-archmap_users.txt``.
    """

    def setUp(self):
        systemd = False
        geojsonio = False

        self.sample_users = "tests/sample-archmap_users.txt"

        self.sample_geojson = "tests/sample-archmap.geojson"
        self.output_geojson = "tests/output-archmap.geojson"
        self.sample_kml = "tests/sample-archmap.kml"
        self.output_kml = "tests/output-archmap.kml"
        self.sample_csv = "tests/sample-archmap.csv"
        self.output_csv = "tests/output-archmap.csv"

        self.parsed_users = archmap.parse_users(self.sample_users, 0)

        # Set 'maxDiff' to 'None' to be able to see long diffs when something goes wrong.
        self.maxDiff = None

    def test_geojson(self):
        archmap.make_geojson(self.parsed_users, self.output_geojson, False, 0)

        with open(self.sample_geojson, "r") as file:
            sample_geojson = file.read()
        with open(self.output_geojson, "r") as file:
           output_geojson = file.read()

        self.assertEqual(sample_geojson, output_geojson)

    def test_kml(self):
        archmap.make_kml(self.parsed_users, self.output_kml, 0)

        with open(self.sample_kml, "r") as file:
            sample_kml = file.read()
        with open(self.output_kml, "r") as file:
            output_kml = file.read()

        self.assertEqual(sample_kml, output_kml)

    def test_csv(self):
        archmap.make_csv(self.parsed_users, self.output_csv, 0)

        with open(self.sample_csv, "r") as file:
            sample_csv = file.read()
        with open(self.output_csv, "r") as file:
            output_csv = file.read()

        self.assertEqual(sample_csv, output_csv)


if __name__ == '__main__':
    unittest.main()
