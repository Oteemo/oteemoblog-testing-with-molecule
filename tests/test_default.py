import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_ntp_is_installed(Package):
    p = Package('ntp')

    assert p.is_installed


def test_ntp_is_started_and_enabled(Service, SystemInfo):
    distro = SystemInfo.distribution
    if distro == 'ubuntu':
        svc = 'ntp'
    elif distro == 'centos':
        svc = 'ntpd'

    s = Service(svc)

    assert s.is_running
    assert s.is_enabled
