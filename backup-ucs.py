"""
Backup UCS-PE settings
Doing this prior to making any changes in Ansible so I can
easily revert to a clean state without running playbooks
to do so.
"""

import sys
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.utils.ucsbackup import backup_ucs

# log into ucsm
handle = UcsHandle("ucs.vm.jm", "ucspe", "ucspe")

# verify successful login
try:
    handle.login()
except URLError:
    sys.exit("Error connecting to UCSM. Check address and credentials.")

# export UCS config

backup_ucs(
    handle, backup_type="config-all", file_dir="./", file_name="ucs-backup_all_pre.xml"
)
