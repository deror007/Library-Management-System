###searches book detail in library list.

def getBookInfo(DatabaseList,bookTitle):


    SearchResult=[]
    SearchResult.append("---------SEARCH FOR BOOK DETAILS:---------")

    bookfound=False 
    
    for bookInfo in DatabaseList:
        bookInfo=bookInfo.replace("\n","")
        BookDetails=bookInfo.split(",")
        '2 is the titles column number starting from 0'
        if bookTitle == BookDetails[2]:
            
            print(BookDetails)
            SearchResult.append(BookDetails)
            
            bookfound=True

    if bookfound==False:
        SearchResult=[]
        SearchResult.append("---------SEARCH FOR BOOK DETAILS:---------")
        print("No book info on given enquiry.")
        SearchResult.append("No book info on given enquiry.")


    return SearchResult





##Testing code is not needed here as they can be evaluated on the GUI

    

