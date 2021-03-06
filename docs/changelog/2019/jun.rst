June 2019
=========

June 25th
---------

.. csv-table:: Module Versions
    :header: "Modules", "Versions"

        ``unicon``, v19.6


Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    bash$ pip install --upgrade unicon


Features and Bug Fixes:
^^^^^^^^^^^^^^^^^^^^^^^

- iosxr plugin

  - Now handling "Enter secret:" and "Enter secret again:" correctly.

  - iosxr/spitfire regex fixes, added init config commands with timeout.

  - spitfire plugin now accepts username and enable password.

- nxos plugin

  - Added guestshell service.

  - Config lock fix

    - add utils method retry_state_machine_go_to

    - add arguments in generic Configure and HaConfigure service for retrying go_to config sate

    - add retry go_to config sate in nxos Reload and HANxosReloadService

    - fix nxos configuration locked problem after reload

  - add nxos n9k plugin whose reload service supports image_to_boot argument


- generic plugin

  - Fix reload service that was hanging when mgmt connection was attempted.

  - Updated execute() service to allow override of default service dialogs by
    passing `service_dialog`

  - improve ping extd_ping judgement and fix endless ping dialog on erroneous
    value

  - Copy service now correctly detects "Could not resolve hostname" as an error

- asa plugin

  - update to handle --more-- prompt.

- ios plugin

  - add iol plugin including switchover support for dIOL devices.

- core

  - modifed ``unicon_record``, ``unicon_replay``, ``unicon_speed`` environment
     variables to ``UNICON_RECORD``, ``UNICON_REPLAY``, and ``UNICON_REPLAY_SPEED``.

  - Disconnect timers may now be updated via Settings object

  - Dialogs are now documented using autogenerated documentation for connect()
    and execute() services.

  - Mock device updates:
    Updated code that replaces the string ESC in prompt with \1xb.
    Print the command that was deemed invalid.
    Added ASA mock device to test more prompt handling.

  - The 'init_exec_commands' and 'init_config_commands' options can now be
    passed via the connection block in the yaml topology file.

  - use SimpleDialogProcessor instead of AlarmBasedDialogProcessor



June 3rd
--------

.. csv-table:: Module Versions
    :header: "Modules", "Versions"

        ``unicon``, v19.5.1


Upgrade Instructions
^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    bash$ pip install --upgrade unicon


Features and Bug Fixes:
^^^^^^^^^^^^^^^^^^^^^^^

- Remove hard ``asyncssh`` package dependency.
  Now users requiring SSH mocks must manually install the
  ``asyncssh`` package.
