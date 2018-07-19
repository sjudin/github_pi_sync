#!/usr/bin/python3
import sys

#TODO: IMPLEMENT WITH GITPYTHON INSTEAD, https://stackoverflow.com/questions/15315573/how-can-i-call-git-pull-from-within-python

from github import Github
from subprocess import Popen, PIPE
from os import path

import time

#time.sleep(15)

test = True

class gitHub(Github):
    def __init__(self, username, password, repo):
        Github.__init__(self, username, password)
        self.repo = self.get_repo(repo)
        self.last_modified = self.get_commits()[0].last_modified

    def get_commits(self):
        commits = list()
        for r in self.repo.get_commits():
                commits.append(r)
        return commits

    def update(self):
        self.last_modified = self.get_commits()[0].last_modified


git = gitHub(sys.argv[1], sys.argv[2], sys.argv[3])
git_command = ['git', 'pull']
repository = path.dirname('/home/pi/projects/' + git.repo.name + '/')

while True:
    previous = git.last_modified
    git.update()
    time.sleep(5)
    if not previous == git.last_modified:
        # repo has been updated, do git pull
        git_query = Popen(git_command, cwd=repository, stdout=PIPE, stderr=PIPE)
        (git_status, error) = git_query.communicate()

        with open('/home/pi/projects/utils/test.log', 'a') as outfile:
            outfile.write(str(git_status))
            outfile.write(str(error))

        if git_query.poll() != 0:
            print(git_status, error)

        git_query.kill()



