'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://twitter.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.generic.patterns import GenericPatterns

class GaiaPatterns(GenericPatterns):
    def __init__(self):
        super().__init__()
        self.password_prompt = r'Password: '
        self.clish_prompt = r'.*> '
        self.login_prompt = r'login: *?'
