from github import Github
from config import config as cfg
import requests

apikey = cfg["GitToken"]
# use your own key
g = Github(apikey)

repo = g.get_repo("rochejamiegmit/ProgrammingForDataAnalysisProject")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

contentOfFile = contentOfFile.replace("Andrew", "Jamie") 

#print (contentOfFile)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
contentOfFile,fileInfo.sha)
