import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_repository_file_exist(host):
    f = host.file('/etc/apt/sources.list.d/spotify.list')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_spotify_is_installed(host):
    spotify = host.package("spotify-client")
    assert spotify.is_installed
