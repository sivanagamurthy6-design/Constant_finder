# Config detector
import re
from app.ast_engine.models import ConstantRecord
from app.detectors.base_detector import BaseDetector
class ConfigDetector(BaseDetector):
    CONFIG_REGEX = re.compile(
        r'((\w+)=([^\s]+))|'  # key=value pairs
        r'((\w+):([^\s]+))'  # key:value pairs
    )
    
    def detect(self, records):
        config_records = []
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and self.CONFIG_REGEX.search(value):
                    config_records.append(record)
        return config_records
