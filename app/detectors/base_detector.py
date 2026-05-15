class BaseDetector:
    def detect(self, records):
        raise NotImplementedError
    

#records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex
    