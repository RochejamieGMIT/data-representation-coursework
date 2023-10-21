import requests
import json
url = "https://andrewbeatty1.pythonanywhere.com/books"

def getallbooks():
    response = requests.get(url)
    return response.json()

def getBookByID(id):
    geturl = url +"/" + str(id)
    response = requests.get(geturl)
    return response.json()

def createBook(book):
    
    response = requests.post(url,json=book)
    return response.json()
 


def updateBook(id, bookdiff):
    updtaeurl = url +"/" + str(id)
    response = requests.put(updtaeurl, json=bookdiff)
    return response.json()

def deleteBook(id):
    deleteurl = url +"/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ =="__main__":
    book = {
        'Author': 'Test', 'Price': 4, 'Title': 'tested'
        }
    
    bookdiff = {
        'Author': 'TestDiff', 'Title': 'testedDiff'
        }
    #print(getallbooks())
    #print(getBookByID(163))
    #print(deleteBook(329))
    #print(createBook(book))
    print (updateBook(331,bookdiff))