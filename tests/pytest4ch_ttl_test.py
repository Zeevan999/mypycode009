"""content of tests for network ttl py test file root directory."""
import pytest

@pytest.fixture
def test_dirs_available(testdir):
    """content of tests for test_dirs_available."""
    result = testdir.runpytest('pytest4ch_ttl_test')
    assert result.ret == 0


class CacheEntry:
    """content of tests for CacheEntry all."""
    def test_method1(self):
        pass

    def test_exitexpired():
        ttl = 0
        assert True


class CacheList:
    """content of tests for CacheList all."""
    def test_method2(self):
        pass

    def add_entry_ttl():
        ttl = 20
        return ttl

    def test_add_entry():
        assert add_entry_ttl() == 20


def test_read_entries():
    string = 'A'
    assert True


def test_read_entries():
    slp = 1
    assert True


def funcexit():
    raise SystemExit(1)


def test_exitsyserror():
    with pytest.raises(SystemExit):
        funcexit()



def test_ok():
    print("ok")


def key_dosent():
    pkey = None
    return pkey


def test_keyfound_fail():
    assert key_dosent() == None


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def incfunc(x):
    return x + 1


def test_answer():
    assert incfunc(4) == 5
