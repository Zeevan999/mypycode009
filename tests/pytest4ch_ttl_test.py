# content of tests for ex CacheListttl py file

from test_ttl_key20 import *
import pytest

@pytest.fixture

def test_dirs_available(testdir):
    result = testdir.runpytest('ch_ttl_test.py')
    assert result.ret == 0
    
def test_exitexpired():
   ttl = 0
   assert  True

def add_entry_ttl():
    ttl = 20
    return ttl
    
    
def test_add_entry():
   
   assert add_entry_ttl() == 20


def test_read_entries():
   string ='A'
   assert True
   
   
def test_read_entries():
    sleep(1)
    assert True
    
    
def funcexit():
    raise SystemExit(1)


def test_exitsyserror():
    with pytest.raises(SystemExit):
        funcexit()

        
def test_error_fixture():
    assert 0


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

    