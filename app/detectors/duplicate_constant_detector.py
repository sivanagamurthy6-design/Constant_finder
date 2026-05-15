# Duplicate constant detector
from app.ast_engine.models import ConstantRecord
from app.detectors.base_detector import BaseDetector
class DuplicateConstantDetector(BaseDetector):
    #records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex
    
    def detect(self, records):
        value_counts = {}
        duplicate_records = []
        
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str):
                    value_counts[value] = value_counts.get(value, 0) + 1
        
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and value_counts[value] > 1:
                    duplicate_records.append(record)
        
        return duplicate_records
