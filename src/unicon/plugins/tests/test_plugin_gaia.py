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

    def test_show_version_all(self):
        r = self.c.execute('show version all')
        r = self.c.command('show version all')
        print(r)

#
    #def test_connect_ssh(self):
    #    c = Connection(hostname='gaia-gw',
    #                    start=['mock_device_cli --os gaia --state connect_ssh'],
    #                    os='gaia',
    #                    credentials=dict(default=dict(
    #                                username='gaia-user', password='gaia-password')))
    #    c.connection_timeout = 1
    #    c.connect()
    #    self.assertIn('gaia-gw>', c.spawn.match.match_output)
    #    c.disconnect()
#
    #def test_login_connect_connectReply(self):
    #    c = Connection(hostname='gaia-gw',
    #                    start=['mock_device_cli --os gaia --state clish'],
    #                    os='gaia',
    #                    credentials=dict(default=dict(
    #                                username='gaia-user', password='gaia-password')),
    #                    connect_reply = Dialog([[r'^(.*?)Password:']]))
    #    c.connection_timeout = 1
    #    c.connect()
    #    self.assertIn("^(.*?)Password:", str(c.connection_provider.get_connection_dialog()))
    #    c.disconnect()

#class TestGaiaPluginExecute(unittest.TestCase):
#
#    def test_execute_show_feature(self):
#        c = Connection(hostname='gaia-gw',
#                        start=['mock_device_cli --os gaia --state shell'],
#                        os='gaia',
#                        credentials=dict(default=dict(
#                                    username='gaia-user', password='gaia-password')))
#        c.connection_timeout = 1
#        c.connect()
#        cmd = 'show version all'
#        expected_response = mock_data['shell']['commands'][cmd].strip()
#        ret = c.execute(cmd).replace('\r', '')
#        self.assertIn(expected_response, ret)
#        c.disconnect()

if __name__ == "__main__":
    unittest.main()
