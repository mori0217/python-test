import os
import pytest


@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.txt'), 'w+') as f:
        print("before yield")
        yield f
        print("after yield")


def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')
