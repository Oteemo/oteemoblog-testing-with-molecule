import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ntp_is_installed(Package):
    p = Package('ntp')

    assert p.is_installed


def test_ntp_is_started_and_enabled(Service):
    s = Service('ntp')

    assert s.is_running
    assert s.is_enabled
