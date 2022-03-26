'''
This file is a container for all modules so that the menu can access
them through. It takes in the inputs and sends back the outputs to the menu.
'''
from booksearch import *
from bookcheckout import *
from bookreturn import *
from bookweed import *
#a list of mini lists containing book and loan history entries

#Used to get updated info
def DatabaseInfo():
    try:
        with open('database.txt') as db: 
            Database_list = db.readlines()
        db.close()
        return Database_list
    except:
        print("ERROR: Database file Cannot be found.")

def LogFileInfo():
    try:
        with open('logfile.txt') as log: 
            Logfile_list = log.readlines()
        log.close()
        return Logfile_list
    except:
                print("ERROR: Log file Cannot be found.")
###      search for book via booksearch.py     ###

def Search_Book(bookTitle):
    Database_list=DatabaseInfo()
    print("---------SEARCH FOR BOOK DETAILS:---------")
    SearchResult=getBookInfo(Database_list,bookTitle)
    return SearchResult


###      Checkout book via bookcheckout.py     ###
def Checkout_A_Book(BookID,MemberID,Day,Month,Year):
    WrongInputs=[]
    Database_list=DatabaseInfo()
    Logfile_list=LogFileInfo()
    print("---------CHECKOUT A BOOK:---------")
    WrongInputs.append("---------CHECKOUT A BOOK:---------")

    #Number of characters in the following if conditions are > 80!! need to shorten

    if IDcheck(MemberID,BookID)==True and Available(BookID,Database_list) == True:
        isBookWithdrawn=withdrawBook(MemberID,BookID,
                                     Database_list,Logfile_list,Day,Month,Year)
        return isBookWithdrawn
    
    elif IDcheck(MemberID,BookID)==False:
        print("ERROR: BOTH MEMBER ID & ID NEED TO BE VALID!")
        WrongInputs.append("ERROR: BOTH MEMBER ID & ID NEED TO BE VALID!")
        return WrongInputs
    elif Available(BookID,Database_list) == False:
        print("Book is not available as it is loaned to another member.")
        WrongInputs.append("Book is unavailable as it is already loaned.")
        return WrongInputs


        
###      return book via returnbook.py     ###
def Return_A_Book(BookID):
    Database_list=DatabaseInfo()
    Logfile_list=LogFileInfo()
    print("---------RETURN A BOOK:---------")

    if checkBookID(BookID) ==  True and isReturned(BookID,Database_list) == True:
        isBookReturned=returnBook(BookID,Database_list,Logfile_list)
        return isBookReturned
    else:
        print("ERROR: The book is not able to be returned.")
        
        noOutput=[]
        noOutput.append("---------RETURN A BOOK:---------")
        noOutput.append("ERROR: The book is not able to be returned.")
        return noOutput
        

def Weed_A_Book(LogFileList,DatabaseList):
    Database_list=DatabaseInfo()
    Logfile_list=LogFileInfo()
    
    LibraryList=getLibraryDataList(LogFileList,DatabaseList)
    getTitleList(LibraryList)
    OutputResults=[]
    OutputResults.append(getPoorQualityTitles(LibraryList))
    OutputResults.append(WithdrawnNo(LibraryList))
    OutputResults.append(getTitleList(LibraryList))
    OutputResults.append(LowWithdrawnTitles(LibraryList))
    OutputResults.append(getWeededTitles(LibraryList))

    
    print("Poor Condition:",getPoorQualityTitles(LibraryList)) 
    print("Low Checkout books:",LowWithdrawnTitles(LibraryList))  
    print("Weeded Books:",getWeededTitles(LibraryList))

    return OutputResults
'''
INPUT TEST CODE FOR ALL BOOK OPERATIONS: (All testing are strings due to the fact that
the client will be accessing the processes via the GUI menu that takes only strings.
Code that was used to deal with wrong data types have been cut out for space and to
make the code simpler. Weed Book operation has no inputs as it searches through the
text files; therefore it is not here.
'''
if __name__ == "__main__":
    #Test different input data for search book.
    Search_Book("book1")
    Search_Book("hg c775dkd")
    Search_Book("")
    #Test different input data for checkout book.
    Checkout_A_Book("12", "7777","11","12","2020")
    Checkout_A_Book("", "","","","")
    Checkout_A_Book("asd", "asd","11","as","asd")
    Checkout_A_Book("12", "7777","11","12","2020") #Repeat again after first time
    #Test different input data for returning a book.
    Return_A_Book("12")
    Return_A_Book("argtea3w")
    Return_A_Book("")


    
