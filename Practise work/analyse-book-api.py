import API_Consuming_with_python as ap

books = ap.getallbooks()
total = 0
count = 0 
for book in books:
    total += book["Price"]
    count += 1

print("Average of count",str(count),"books is ",str(total/count))