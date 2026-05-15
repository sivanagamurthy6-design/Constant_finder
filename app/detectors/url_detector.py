# URL detector
import re
from app.ast_engine.models import ConstantRecord
from app.detectors.base_detector import BaseDetector
class URLDetector(BaseDetector):
    URL_REGEX = re.compile(
        r'((http|https)://)?'  # optional scheme
        r'([a-zA-Z0-9.-]+)'  # domain
        r'(\.[a-zA-Z]{2,})'  # top-level domain
        r'(:\d+)?'  # optional port
        r'(/[\w./?%&=-]*)?'  # optional path and query
    )
    
    def detect(self, records):
        url_records = []
        #print(f"Detecting URLs in records: {records}")
        #records are in the form of list of ConstantRecord objects,
        # # we need to extract the value from each record and check if it matches the URL regex
        for record in records:
            if isinstance(record, ConstantRecord):
                value = record.value
                if isinstance(value, str) and self.URL_REGEX.search(value):
                    url_records.append(record)
        return url_records