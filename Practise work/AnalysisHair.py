from ValOfficeDataConsumption import getall

data = getall()
totalArea = 0
for entry in data:
    valuationreports = entry["ValuationReport"]
    #print(valuationreports)
    for valuationreport in valuationreports:
        #print(valuationreport)
        if valuationreport["FloorUse"] == "RESTAURANT":
            totalArea = totalArea + valuationreport["Area"]
            #print(valuationreport["Area"],"+",totalArea,end="")    
print(totalArea)