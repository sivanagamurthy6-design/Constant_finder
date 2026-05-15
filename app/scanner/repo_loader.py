# Repository loading logic
from app.scanner.git_handler import GitHandler
from app.scanner.file_scanner import FileScanner
class RepoLoader:
    def __init__(self):
        self.git_handler = GitHandler()
        self.file_scanner = FileScanner()
    
    #if the repository already exists again clone it, just return the path to the repository
    def load_repository(self, repo_url, destination):
        if repo_url:
            if self.git_handler.repository_exists(destination):
                print(f"Repository already exists at {destination}. Pulling latest changes...")
                self.git_handler.pull_repository(destination)
                print(f"Repository at {destination} is up to date.")
            else:
                self.git_handler.clone_repository(repo_url, destination)
        else:
            print("No repository URL provided. Checking for local directory...")
            #copy the local directory to the destination and scan it for files
            self.git_handler.copy_local_directory(destination)
        print(f"Scanning repository at {destination} for Python files...")
        files = self.file_scanner.scan(destination)
        return files
        
    
