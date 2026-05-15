# Console report generator
from .base_report import BaseReport
class ConsoleReport(BaseReport):
    def generate(self, findings):
        for finding in findings:
            print(f"File: {finding.file_path}, Line: {finding.line_number}, Issue: {finding.issue_type}, Value: {finding.value}")   

