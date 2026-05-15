#base report
class BaseReport:
    def generate(self, findings):
        raise NotImplementedError("Subclasses must implement this method")