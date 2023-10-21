import requests
import json

urlBegin = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def CSOgetAllAsFile(dataset):
    with open("TestCSO.json","wt") as fp:
        print(json.dumps(CSOgetAll(dataset)), file = fp)

def CSOgetAll(dataset):
    url = urlBegin + dataset + urlEnd
    response = requests.get(url)
    return response.json()


def CSOGetFormattedAsFile(dataset):
    pass

def CSOgetAllFormatted(dataset):
    data = CSOgetAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]

    for dim0 in range(0, sizes[0]):
        CurrentID = ids[0]
        index = dimensions[CurrentID]["category"]["index"][dim0]
        label = dimensions[CurrentID]["category"]["index"]
        print(label)
        for dim1 in range(0, sizes[1]):
            CurrentID = ids[1]
            index = dimensions[CurrentID]["category"]["index"][dim1]
            label = dimensions[CurrentID]["category"]["index"]
            print("\t", label)
            for dim2 in range(0, sizes[2]):
                CurrentID = ids[2]
                index = dimensions[CurrentID]["category"]["index"][dim2]
                label = dimensions[CurrentID]["category"]["index"]
                print("\t\t", label)
                for dim3 in range(0, sizes[3]):
                    CurrentID = ids[3]
                    index = dimensions[CurrentID]["category"]["index"][dim3]
                    label = dimensions[CurrentID]["category"]["index"]
                    print("\t\t\t", label)
   

if __name__ == "__main__":
    dataset = "FP001"
    #CSOgetAllAsFile(dataset)
    CSOgetAllFormatted(dataset)