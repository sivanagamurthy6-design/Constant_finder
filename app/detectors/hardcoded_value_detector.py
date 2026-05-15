# Hardcoded value detector
from app.detectors.base_detector import BaseDetector
from app.ast_engine.constant_extractor import ConstantExtractor
from app.ast_engine.ast_parser import ASTParser
from app.ast_engine.models import ConstantRecord
from typing import List, Optional
class HardcodedValueDetector(BaseDetector):
    #records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex

    def detect(self, records):
        hardcoded_records = []
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and not value.strip().startswith(('http', 'https', 'password', 'secret', 'api_key', 'token', 'credential')):
                    hardcoded_records.append(record)
        return hardcoded_records
    
