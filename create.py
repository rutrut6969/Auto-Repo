import sys
import os
from github import Github


project = r"C:\Users\rutle\OneDrive\Documents\Code Projects"
git_user = "rutrut6969"
git_pass = "Rutledge69"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(project + str(sys.argv[1]))
    user = Github(git_user, git_pass).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))


if __name__ == "__main__":
    create()