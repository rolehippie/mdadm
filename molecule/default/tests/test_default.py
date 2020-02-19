import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_mdadm_is_installed(host):
    mdadm = host.package("mdadm")
    assert mdadm.is_installed
