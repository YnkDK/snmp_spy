from io import StringIO

from behave import given, when, then
from os.path import dirname, realpath, join
from unittest import mock
from snmp_spy.cli import main


@given('an SNMP walk output')
def step_impl(context):
    root_path = dirname(dirname(realpath(__file__)))
    data_path = join(root_path, 'examples', 'data')

    context.snmpwalk_path = join(data_path, 'synology.snmpwalk')


@when('the command-line interface is lunched')
def step_impl(context):
    with mock.patch('sys.argv', ['cli', '-f', context.snmpwalk_path]), \
            mock.patch('sys.stdout', new_callable=StringIO) as stdout:
        main()

        context.stdout = stdout


@then('all objects are shown')
def step_impl(context):
    stdout = context.stdout.getvalue()  # type: str
    lines = stdout.splitlines()
    last_line = lines[-1]
    assert last_line.startswith("386)"), f"Got: {last_line}"
