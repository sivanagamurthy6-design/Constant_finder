# JSON report generator
import json
from .base_report import BaseReport
class JSONReport(BaseReport):
    def generate(self, findings):
        report_data = []
        for finding in findings:
            report_data.append({
                "file_path": finding.file_path,
                "line_number": finding.line_number,
                "issue_type": finding.issue_type,
                "value": finding.value
            })
        return json.dumps(report_data, indent=4)
