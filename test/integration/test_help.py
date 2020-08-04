import re


def test_help(cli):
    result = cli('ansible-builder --help', check=False)
    help_text = result.stdout
    assert 'usage: ansible-builder [-h] [--version] {build,introspect}' in help_text


def test_no_args(cli):
    result = cli('ansible-builder', check=False)
    stderr = result.stderr
    assert 'usage: ansible-builder [-h] [--version] {build,introspect}' in stderr
    assert 'ansible-builder: error: the following arguments are required: action' in stderr


def test_version(cli):
    result = cli('ansible-builder --version')
    version = result.stdout
    matches = re.findall(r'\d.\d.\d', version)
    assert matches
