from tests.utils import ExpectedDict


class BaseTest:
    def test_valid(self):
        assert {"a": True} == ExpectedDict({"a": True})

    def test_invalid(self):
        assert {"a": True} == ExpectedDict({"a": False})


class TestImplementation(BaseTest):
    pass
