# Security-related rules
from app.rules.constants_rules import ConstantRules
from app.rules.config_rules import ConfigRules
class SecurityRules:
    def __init__(self):
        self.constant_rules = ConstantRules()
        self.config_rules = ConfigRules()
    
    def apply_rules(self, records):
        findings = []
        
        findings.extend(self.constant_rules.apply_rules(records))
        findings.extend(self.config_rules.apply_rules(records))
        
        return findings
