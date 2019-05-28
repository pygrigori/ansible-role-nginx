import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_pkg_installed(host):
    package = host.package('nginx')

    assert package.is_installed


def test_service_is_enabled(host):
    service = host.service('nginx')

    assert service.is_enabled


def test_config_exists(host):
    file = host.file('/etc/nginx/nginx.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_config_is_valid(host):
    cmd = host.run('nginx -t')

    assert not cmd.rc
