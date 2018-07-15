import os
import pytest

@pytest.fixture
def csv_file(tmpdir):
    # return 'csv file!!!'
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('beafore test')
        yield c
        print('after test')

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')
