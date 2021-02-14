'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://twitter.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

from unicon.plugins.generic import GenericSingleRpConnection, ServiceList
from unicon.plugins.generic.connection_provider import GenericSingleRpConnectionProvider
from .statemachine import GaiaStateMachine
from .services import GaiaServiceList
from . import services as gaia_services
from .settings import GaiaSettings
from . import service_implementation as gaia_svc
from unicon.plugins.generic import ServiceList, service_implementation as svc

class GaiaConnectionProvider(GenericSingleRpConnectionProvider):
    pass

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

class GaiaServiceList(ServiceList):
    def __init__(self):
        self.execute = svc.Execute
        self.sendline = svc.SendLine