'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://twitter.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''
import logging

from unicon.bases.linux.services import BaseService
from unicon.plugins.generic.service_implementation import Execute as GenericExec
from unicon.plugins.ios.iosv import IosvServiceList
from . import service_implementation as gaia_svc
from unicon.plugins.generic import service_implementation as svc
logger = logging.getLogger(__name__)


class Execute(GenericExec):
    '''
    Demonstrating how to augment an existing service by updating its call
    service method
    '''

    def __init__(self, connection, context, **kwargs):
        # Connection object will have all the received details
        super().__init__(connection, context, **kwargs)
        self.service_name = 'execute'
        self.timeout = connection.settings.EXEC_TIMEOUT
        self.__dict__.update(kwargs)

    def call_service(self, *args, **kwargs):
        # custom... code here
        logger.info('execute service called')
    
        # call parent
        super().call_service(*args, **kwargs)

#class GaiaService(BaseService):
#    '''
#    demonstrating the implementation of a local, new service
#    '''
#
#    def call_service(self, *args, **kwargs):
#        logger.info('imaginary service called!')
#        return 'Gaiaos' * 3


class GaiaServiceList():
    '''
    class aggregating all service lists for this platform
    '''

    def __init__(self):
        # use the parent servies
        super().__init__()

        # overwrite and add our own
        self.execute = Execute
        self.sendline = svc.SendLine
        #self.gaiaos = GaiaService
