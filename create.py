import sys
import os
from github import github

path = "C:\Users\rutle\OneDrive\Documents\Code Projects"
git_user = "rutrut6969"
git_pass = "Rutledge69"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = github(git_user, git_pass).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))


if __name__ == "__main__":
    create()