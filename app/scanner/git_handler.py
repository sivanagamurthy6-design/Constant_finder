# Git repository handling
import os
from os import path, stat
from importlib.resources import path
import subprocess
import stat
import shutil
from datetime import datetime

class GitHandler:
    
    def clone_repository(self, repo_url, destination):
        try:
            subprocess.run(['git', 'clone', repo_url, destination], check=True)
            print(f"Repository cloned to {destination}")
        except subprocess.CalledProcessError as e:
            print(f"Error cloning repository: {e}")
    def repository_exists(self, destination):
        try:
            subprocess.run(['git', '-C', destination, 'status'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False
    def pull_repository(self, destination):

        subprocess.run(
        ['git', '-C', destination, 'reset', '--hard'],
        check=True
                        )
        
        subprocess.run(
            ['git', '-C', destination, 'pull'],
            check=True
        )

        print(f"Repository updated: {destination}")

    def _remove_readonly(self, func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    def create_backup(self, source_folder):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_folder = rf"D:\repo_backups\backup_{timestamp}"

        shutil.copytree(source_folder, backup_folder)

        print(f"Backup created at: {backup_folder}")

    def copy_local_directory(self, source_folder, destination):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if os.path.exists(destination):
            print(f"Destination folder already exists: {destination}")
            # instead of deleting the destination folder, create a backup of the destination folder and over ride the destination folder with the source folder
            self.create_backup(destination)
            os.chmod(destination, stat.S_IWRITE)
            shutil.rmtree(destination, 
                          onerror=self._remove_readonly)
            print(f"Existing destination folder deleted: {destination}")
            shutil.copytree(source_folder, destination, ignore=shutil.ignore_patterns(".git"))
            print(f"Local directory copied to {destination} at date and time: {timestamp}")
        else:
            print(f"Destination folder does not exist: {destination}")
            shutil.copytree(source_folder, destination, ignore=shutil.ignore_patterns(".git"))
            print(f"Local directory copied to {destination} at date and time: {timestamp}")


    def delete_backup(self, backup_folder):
        if os.path.exists(backup_folder):
            shutil.rmtree(backup_folder)
            print(f"Backup deleted: {backup_folder}")
        else:
            print(f"Backup folder not found: {backup_folder}")