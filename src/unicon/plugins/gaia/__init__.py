'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://github.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.generic import GenericSingleRpConnection, ServiceList
from unicon.plugins.generic import service_implementation as svc
from unicon.plugins.generic.connection_provider import GenericSingleRpConnectionProvider


from .statemachine import GaiaStateMachine
from .settings import GaiaSettings

class GaiaConnectionProvider(GenericSingleRpConnectionProvider):
    """
        Connection provider class for gaia connections.
    """
    pass

class GaiaServiceList(ServiceList):
    """ gaia services """
    def __init__(self):
        #super().__init__()
        self.execute = svc.Execute
        self.sendline = svc.Sendline

class GaiaConnection(GenericSingleRpConnection):
    '''GaiaosSingleRPConnection

    Gaia platform support. 
    '''
    os = 'gaia'
    platform = None
    chassis_type = 'single_rp'
    state_machine_class = GaiaStateMachine
    connection_provider_class = GaiaConnectionProvider
    subcommand_list = GaiaServiceList
    settings = GaiaSettings()