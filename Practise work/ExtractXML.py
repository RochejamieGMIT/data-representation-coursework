from xml.dom.minidom import parse
filename = "TestXML.xml"

# read file in 2 ways
doc = parse(filename)

# or 
# with open(filename) as fp:
#   doc = parse(fp)

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList)) # check how many names are there
for employeeNode in employeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)
