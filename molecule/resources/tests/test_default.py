import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("repo_file", [
    ("/etc/yum.repos.d/elastic-7.x.repo")
])

def test_repo(host, repo_file):
    assert host.file(repo_file).exists
