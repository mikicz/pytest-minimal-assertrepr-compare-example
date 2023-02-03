

class ExpectedDict:

    def __init__(self, expected):
        self.expected = expected
        self.errors = []

    def __eq__(self, other):
        if other is None:
            self.errors.append("Other is None.")
            return False

        self.errors = []
        for k, v in self.expected.items():
            key_message = str(k)

            if k not in other:
                self.errors.append(f"{key_message}: not found")
            else:
                if v != other[k]:
                    self.errors.append(f"{k}: {v!r} != {other[k]!r}")

        return not self.errors

    def __repr__(self):
        return str(self.errors)
