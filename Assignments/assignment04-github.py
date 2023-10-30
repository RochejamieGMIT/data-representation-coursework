from github import Github
from config import config as cfg
import requests

apikey = cfg["GitToken"]
# use your own key
GAccess = Github(apikey)

repo = GAccess.get_repo("rochejamiegmit/ProgrammingForDataAnalysisProject")
#print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
RepoLocation = fileInfo.download_url

#print (urlOfFile)

response = requests.get(RepoLocation)
TestText = response.text
#print (contentOfFile)

TestText = TestText.replace("Andrew", "Jamie") 

#print (contentOfFile)

gitHubResponse=repo.update_file(fileInfo.path,"replace Andrew With Jamie",
TestText,fileInfo.sha)
