from github import Github
g=Github("pythongiant","srihari7")
repos=""
new_reps=""
def train():
    global repos
    for repo in g.get_user().get_repos():
        file=open("repos.txt","a+")
        file.write(repo.name+"\n")
        repos+=file.read()
        print(repo.name)
def test():
    global new_reps
    for repo in g.get_user().get_repos():
        file=open("New_Repos.txt","a+")
        file.write(repo.name+"\n")
        new_reps+=file.read()
    if new_reps != repos:
        print("all right")
    else:
        print("nope! new stuff is there")    