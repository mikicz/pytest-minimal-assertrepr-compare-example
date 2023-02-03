from tests.utils import ExpectedDict

class TestX():
    def test_valid(self):
        assert {"a": True} == ExpectedDict({"a": True})


    def test_invalid(self):
        assert {"a": True} == ExpectedDict({"a": False})
