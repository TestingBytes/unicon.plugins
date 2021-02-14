


from unicon.core.errors import SubCommandFailure, StateMachineError
from unicon.bases.routers.services import BaseService
from unicon.eal.dialogs import Dialog, Statement
from unicon.logs import UniconStreamHandler

from unicon.plugins.generic.service_implementation import Execute as GenericExecute
from unicon.plugins.generic.statements import GenericStatements
from unicon.plugins.generic import GenericUtils
from unicon.plugins.utils import slugify

class Command(BaseService):
    """ Service to execute a single command on the ConfD CLI.
    This service is used by the Configure and Execute services
    to execute a single command. Command output is checked for errors
    as part of the services implementation in bases.routers.services.

    Arguments:
        command: command string
        reply: Addition Dialogs for interactive config commands.
        timeout : Timeout value in sec, Default Value is 60 sec

    Returns:
        Command output string
        raise SubCommandFailure on failure
        raise StateMachineError if CLI state is not supported

    Example:
        .. code-block:: python

              output = device.command('show services')

    """

    def __init__(self, connection, context, **kwargs):
        super().__init__(connection, context, **kwargs)
        self.timeout_pattern = ['Timeout occurred', ]
        self.result = None
        self.timeout = connection.settings.EXEC_TIMEOUT

    def log_service_call(self):
        pass

    def pre_service(self, *args, **kwargs):
        pass

    def post_service(self, *args, **kwargs):
        pass

    def call_service(self, command,
                     reply=Dialog([]),
                     timeout=None,
                     error_pattern=None,
                     *args, **kwargs):

        con = self.connection

        timeout = timeout or self.timeout
        if error_pattern is None:
            self.error_pattern = con.settings.ERROR_PATTERN
        else:
            self.error_pattern = error_pattern

        if not isinstance(command, str):
            raise SubCommandFailure('Command is not a string: %s' % type(command))

        sm = self.get_sm()

        con.log.info("+++ command '%s' +++" % command)
        timeout = timeout or con.settings.EXEC_TIMEOUT
        if not isinstance(reply, Dialog):
            raise SubCommandFailure(
                "dialog passed via 'reply' must be an instance of Dialog")

        dialog = Dialog()
        if reply:
            dialog += reply
        for state in sm.states:
            dialog.append(Statement(pattern=state.pattern))
        # dialog.append(statements.more_prompt_stmt)

        con.sendline(command)
        try:
            self.result = dialog.process(con.spawn, timeout=timeout, context=self.context)
        except Exception as err:
            raise SubCommandFailure("Command execution failed", err)

        if self.result:
            self.result = self.result.match_output

        sm.detect_state(con.spawn)
        self.end_state = sm.current_state
