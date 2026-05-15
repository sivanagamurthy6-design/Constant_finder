# Credential detector
import re
from app.ast_engine.models import ConstantRecord
from app.detectors.base_detector import BaseDetector
class CredentialDetector(BaseDetector):
    CREDENTIAL_REGEX = re.compile(
        r'((password|secret|api[_-]?key|token|credential)[\s:=]+[^\s]+)', re.IGNORECASE
    )
    #records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex

    
    def detect(self, records):
        credential_records = []
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and self.CREDENTIAL_REGEX.search(value):
                    credential_records.append(record)
        return credential_records
