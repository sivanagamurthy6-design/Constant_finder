import os
from app.ast_engine.constant_extractor import ConstantExtractor
from app.ast_engine.ast_parser import ASTParser
from app.detectors.url_detector import URLDetector
from app.scanner.repo_loader import RepoLoader
from app.detectors.credential_detector import CredentialDetector
from app.detectors.hardcoded_value_detector import HardcodedValueDetector
from app.detectors.constant_detector import ConstantDetector
from app.detectors.duplicate_constant_detector import DuplicateConstantDetector
from app.detectors.url_detector import URLDetector
from app.detectors.base_detector import BaseDetector
from app.scanner.git_handler import GitHandler



def main(path_to_scan):
    # Initialize the repository loader and Git handler
    repo_loader = RepoLoader()
    git_handler = GitHandler()
    #constant_extractor = ConstantExtractor()
    parser = ASTParser()

    #first check whether the repo is given or local directory is given, if the repo is given then clone it to the destination and scan it for files, if the local directory is given then copy it to the destination and scan it for files
    if path_to_scan.startswith("http"):
        repo_loader.load_repository(path_to_scan, "temp_repo")
        python_files = repo_loader.file_scanner.scan("temp_repo")
        print(f"Python files found in repository: {python_files}")
    else:
        git_handler.copy_local_directory(path_to_scan, "temp_repo")
        python_files = repo_loader.file_scanner.scan("temp_repo")
        print(f"Python files found in {path_to_scan}: {python_files}")
    # Initialize detectors
    url_detector = URLDetector()
    credential_detector = CredentialDetector()
    hardcoded_value_detector = HardcodedValueDetector()
    constant_detector = ConstantDetector()
    duplicate_constant_detector = DuplicateConstantDetector()

    # Scan each file for hardcoded values
    for file in python_files:
        print(f"Scanning {file} for hardcoded values...")
        #read the file content
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
            #print(f"File content of {file}:\n{file_content}\n")
            record = parser.parse(file_content, file)
            #print(f"Parsed records:{record}")
            # for r in record:
            #     print(f"  - {r}")

            url_issues = url_detector.detect(record)
            credential_issues = credential_detector.detect(record)
            hardcoded_value_issues = hardcoded_value_detector.detect(record)
            constant_issues = constant_detector.detect(record)
            duplicate_constant_issues = duplicate_constant_detector.detect(record)

            # Print detected issues
            if url_issues:
                print(f"URL issues found in {file}: {url_issues}")
            if credential_issues:
                print(f"Credential issues found in {file}: {credential_issues}")
            if hardcoded_value_issues:
                print(f"Hardcoded value issues found in {file}: {hardcoded_value_issues}")
            if constant_issues:
                print(f"Constant issues found in {file}: {constant_issues}")
            if duplicate_constant_issues:
                print(f"Duplicate constant issues found in {file}: {duplicate_constant_issues}")
if __name__ == "__main__":
    main("D:\\repo_backups\\backup_20260512_111153")
