"""
Unittests for Gaia plugin

"""

__author__ = "Sam Johnson <samuel.johnson@gmail.com>"

import os
import yaml
import unittest
from unittest.mock import patch

import unicon
from unicon import Connection
from unicon.eal.dialogs import Dialog
from unicon.mock.mock_device import mockdata_path

with open(os.path.join(mockdata_path, 'gaia/gaia_mock_data.yaml'), 'rb') as datafile:
    mock_data = yaml.safe_load(datafile.read())


class TestGaiaPlugin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.c = Connection(hostname='gaia-gw',
                        start=['/pyats/bin/mock_device_cli --os gaia --state login'],
                        os='gaia',
                        credentials={'default': {'username':'gaia-user', 'password':'gaia-password'}}
                        )
        #cls.c.connection_timeout = 1
        cls.c.connect()

    def test_execute(self):
        r = self.c.execute('show version all')
        self.assertIn("Product version",r)

if __name__ == "__main__":
    unittest.main()
