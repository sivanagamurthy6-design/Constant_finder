# Config-related rules
from app.detectors.config_detector import ConfigDetector
from app.detectors.credential_detector import CredentialDetector
from app.detectors.hardcoded_value_detector import HardcodedValueDetector
from app.detectors.duplicate_constant_detector import DuplicateConstantDetector
class ConfigRules:
    def __init__(self):
        self.config_detector = ConfigDetector()
        self.credential_detector = CredentialDetector()
        self.hardcoded_value_detector = HardcodedValueDetector()
        self.duplicate_constant_detector = DuplicateConstantDetector()
    
    def apply_rules(self, records):
        findings = []
        
        findings.extend(self.config_detector.detect(records))
        findings.extend(self.credential_detector.detect(records))
        findings.extend(self.hardcoded_value_detector.detect(records))
        findings.extend(self.duplicate_constant_detector.detect(records))
        
        return findings
