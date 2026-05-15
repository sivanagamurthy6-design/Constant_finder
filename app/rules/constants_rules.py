# Constant detection rules  
from app.detectors.constant_detector import ConstantDetector
from app.detectors.duplicate_constant_detector import DuplicateConstantDetector
class ConstantRules:
    def __init__(self):
        self.constant_detector = ConstantDetector()
        self.duplicate_constant_detector = DuplicateConstantDetector()
    
    def apply_rules(self, records):
        findings = []
        
        findings.extend(self.constant_detector.detect(records))
        findings.extend(self.duplicate_constant_detector.detect(records))
        
        return findings
    
