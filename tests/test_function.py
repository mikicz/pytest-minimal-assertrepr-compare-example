from tests.utils import ExpectedDict


def test_valid():
    assert {"a": True} == ExpectedDict({"a": True})


def test_invalid():
    assert {"a": True} == ExpectedDict({"a": False})
