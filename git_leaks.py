#usr/bin/python

from git import Repo
import re, signal, sys, time, pwn, pdb, os    # Librerías que no te hace falta instalar


#iter commit lo metemos en una lista, le dicmos el max numero de commit (todos) 
def handler_signal(signal, frame):
    print("\n\n [!] Out ....... \n")
    sys.exit(1)
# Ctrl + C
signal.signal(signal.SIGINT, handler_signal)

def extract(path):
    repo = Repo(path)       # Crea un objeto que te permite interactuar con el repositorio que hay en el path
    return repo.iter_commits()

def transform(commits, length):
    progress = [" " for i in range(102)]
    progress[0] = "["
    progress[-1] = "]"
    all_matches = []

    print("Progress:\t", end = "")
    for i in range(len(progress)):
        print(progress[i], end = "")
    print(f"\t0 %")
    
    count = 0
    index = int(count * 100 / length)

    pattern = re.compile(r".{10}private[-.\s]keys.{10}", re.IGNORECASE)

    for commit in commits:
        matches = pattern.finditer(commit.message)
        for match in matches:
            if match != None:
                all_matches.append(match)
        
        count += 1
        if index != int(count * 100 / length):
            os.system('cls||clear')
            progress[index + 1] = ">"
            print("Progress:\t", end = "")
            for i in range(len(progress)):
                print(progress[i], end = "")
            print(f"\t{index} %")
            index = int(count * 100 / length)

    os.system('cls||clear')
    print("Progress:\t", end = "")
    for i in range(len(progress)):
        print(progress[i], end = "")
    print(f"\t100 %")
    print("Finished!")

    return all_matches

def load(all_matches):
    for match in all_matches:
        print(match)


if __name__ == "__main__":
    REPO_DIR = "./skale/skale-manager"
    commits = extract(REPO_DIR)
    length = len(list(commits))
    all_matches = transform(extract(REPO_DIR), length)
    load(all_matches)