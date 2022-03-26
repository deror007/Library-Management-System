#WEEDED BOOKS = BOOK'S CHECKOUTNUMBER <5 + "POOR" CONDITION <- explained better
#in README text file.
'''
The weeding criteria depends on the number of withdrawns of a book and
its condition. If a book is withdrawn less than 5 times and is in a "POOR"
condition, it will be weeded from the library.
'''
def getWeededTitles(LibraryList):
    WeededTitles=[]
    for poorTitle in getPoorQualityTitles(LibraryList):
        for lowWithdrawnTitle in LowWithdrawnTitles(LibraryList):
            if poorTitle == lowWithdrawnTitle:
                WeededTitles.append(poorTitle)
                
    return (WeededTitles)

def LowWithdrawnTitles(LibraryList):
    
    MinimumCheckoutNo = 5
    lowWithdrawnTitles=[]
    for Entry in LibraryList:
        if int(Entry[3])< MinimumCheckoutNo:
            lowWithdrawnTitles.append(Entry[6])
           
    return (lowWithdrawnTitles)

def WithdrawnNo(LibraryList):
    
    MinimumCheckoutNo = 5
    WithdrawnNos=[]
    for Entry in LibraryList:
        WithdrawnNos.append(int(Entry[3]))
           
    return (WithdrawnNos)


def getPoorQualityTitles(LibraryList):
    poorTitles=[]
    for Entry in LibraryList:
        if Entry[4]=="POOR":
            poorTitles.append(Entry[6])
            
    return (poorTitles)
    
'''
Combines loglist and database list to help collect info on both files easier.
'''
                
def getLibraryDataList(DatabaseList,LogFileList):

    LibraryData_list=[]

    for bookinfo in DatabaseList:
        BookEntry= bookinfo.replace("\n","")
        BookEntry = BookEntry.split(",")
        
        for loginfo in LogFileList:
            LogEntry= loginfo.replace("\n","")
            LogEntry = LogEntry.split(",")
            
            if BookEntry[0] == LogEntry[0]:
                BookEntry.extend(LogEntry)
                del(BookEntry[6])

                LibraryData_list.append(BookEntry)
    LibraryData_list.remove(LibraryData_list[0])

    return(LibraryData_list)


def getTitleList(LibraryList):

    TitleList=[]

    for bookinfo in LibraryList:
        TitleList.append(bookinfo[6])    


    return TitleList

## Test Weeding via pressing "WEED LIBRARY" on the GUI menu.
##To see barchart update; run checkout book with successful inputs and
##run "weeding library" again.

