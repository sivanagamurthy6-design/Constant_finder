# File scanning logic
import os
class FileScanner:
    def scan(self, directory):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith('.py'):
                    files.append(os.path.join(root, filename))
        return files
    
