#constant detectors
from app.ast_engine.models import ConstantRecord
from app.detectors.base_detector import BaseDetector
class ConstantDetector(BaseDetector):
    #records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex
    
    def detect(self, records):
        constant_records = []
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and value.isupper() and len(value) > 1:
                    constant_records.append(record)
        return constant_records