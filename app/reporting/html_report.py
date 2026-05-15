# HTML report generator
from .base_report import BaseReport
class HTMLReport(BaseReport):
    def generate(self, findings):
        html = "<html><head><title>Hardcoding Detection Report</title></head><body>"
        html += "<h1>Hardcoding Detection Report</h1>"
        html += "<table border='1'><tr><th>File</th><th>Line</th><th>Issue</th><th>Value</th></tr>"
        
        for finding in findings:
            html += f"<tr><td>{finding.file_path}</td><td>{finding.line_number}</td><td>{finding.issue_type}</td><td>{finding.value}</td></tr>"
        
        html += "</table></body></html>"
        return html
