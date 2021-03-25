'''
Author: Sam Johnson
Contact: samuel.johnson@gmail.com
https://github.com/TestingBytes

Contents largely inspired by sample Unicon repo:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''

#from unicon.core.errors import SubCommandFailure
#from unicon.bases.routers.services import BaseService
#from unicon.eal.dialogs import Dialog, Statement

#class Command(BaseService):
#
#    def __init__(self, connection, context, **kwargs):
#        super().__init__(connection, context, **kwargs)
#        self.timeout_pattern = ['Timeout occurred', ]
#        self.result = None
#        self.timeout = connection.settings.EXEC_TIMEOUT
#
#    def log_service_call(self):
#        pass
#
#    def pre_service(self, *args, **kwargs):
#        pass
#
#    def post_service(self, *args, **kwargs):
#        pass
#
#    def call_service(self, command,
#                     reply=Dialog([]),
#                     timeout=None,
#                     error_pattern=None,
#                     *args, **kwargs):
#
#        con = self.connection
#
#        timeout = timeout or self.timeout
#        if error_pattern is None:
#            self.error_pattern = con.settings.ERROR_PATTERN
#        else:
#            self.error_pattern = error_pattern
#
#        if not isinstance(command, str):
#            raise SubCommandFailure('Command is not a string: %s' % type(command))
#
#        sm = self.get_sm()
#
#        con.log.info("+++ command '%s' +++" % command)
#        timeout = timeout or con.settings.EXEC_TIMEOUT
#        if not isinstance(reply, Dialog):
#            raise SubCommandFailure(
#                "dialog passed via 'reply' must be an instance of Dialog")
#
#        dialog = Dialog()
#        if reply:
#            dialog += reply
#        for state in sm.states:
#            dialog.append(Statement(pattern=state.pattern))
#        # dialog.append(statements.more_prompt_stmt)
#
#        con.sendline(command)
#        try:
#            self.result = dialog.process(con.spawn, timeout=timeout, context=self.context)
#        except Exception as err:
#            raise SubCommandFailure("Command execution failed", err)
#
#        if self.result:
#            self.result = self.result.match_output
#
#        sm.detect_state(con.spawn)
#        self.end_state = sm.current_state
#