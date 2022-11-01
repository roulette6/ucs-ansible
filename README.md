# Ansible Cisco UCSM
This project uses Cisco UCSM Platform Emulator to test Ansible and Python projects. The list of Cisco UCS modules can be found by running `ansible-doc -l | grep ucs` or by going to the [Cisco UCS Ansible Galaxy page](https://galaxy.ansible.com/cisco/ucs).

## Setup
* Spin up the Cisco UCS-PE VM. The default username and password are both `ucspe`.
* This repo includes a full config before any changes are made via Ansible.
  - You can roll back to this state by running the __restore-ucs.py__ script or by changing the state to `absent` on the playbooks.

## Files
* __backup-ucs.py:__ Python script used to back up the settings prior to making any changes.
* __restore-ucs.py:__ Python script to clean the slate in lieu of having playbooks to delete things.
* __ucs-backup_all_pre.xml:__ Clean slate full config (before anything was created)
* __ansible.cfg:__ Settings to indicate inventory and to suppress warnings about python3.
* __inventory.yml:__ Ansible Inventory of UCS domains.
* __orgs.yml:__ Ansible playbook to create two orgs with one sub-org each.
* __ntwk-components.yml:__ Ansible playbook to create VLANs, vNIC templates, and LAN connectivity policies.
* __ucs-control.yml:__ Ansible playbook to call orgs.yml and ntwk-components.yml, in that order.