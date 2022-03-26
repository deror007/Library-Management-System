'''
returning a book would cause the return date column
in logfile.txt to "NONE" for the intended bookID's record.
DBFiles' memberID = "0000" and LogFiles checkoutDate and returnDate = "NONE"
'''

def isReturned(BookID,DatabaseList):
                    #Check wanted book is needed to return
    checker=False
    for bookinfo in DatabaseList:
        bookinfo=bookinfo.replace("\n","")
        BookEntry=bookinfo.split(",")

        if "0000" != BookEntry[5] and BookID == BookEntry[0]:
            checker = True
            return True
        
    if checker == False:
        return False

def returnBook(BookID,DatabaseList,LogFileList):
    ReturnResults = []
    ReturnResults.append("---------RETURN A BOOK:---------")
    
    BookReturned=False
        #updated availability of given ID's in Database.txt
    dbFile = open("database.txt","w")
    for f_record in DatabaseList: 
        f_record=f_record.replace("\n","")
        f_record=f_record.split(",")

        if BookID == f_record[0]:
            f_record.insert(5,"0000")
            del(f_record[6])
            
            print("Updated Book Details:",f_record)
            ReturnResults.append("Updated Book Details:")
            ReturnResults.append(f_record)
            
        # add each line back to .txt file after update.
        Updated_record=",".join(f_record)
        dbFile.writelines(Updated_record+"\n")
    dbFile.close()


    #updated loan history of given ID's in Logfile.txt
    logFile = open("logfile.txt","w")
    for loan_record in LogFileList: 
        loan_record=loan_record.replace("\n","")
        loan_record=loan_record.split(",")

        if BookID == loan_record[0]:
            loan_record.insert(1,"NONE")
            del(loan_record[2])
            loan_record.insert(2,"NONE")
            del(loan_record[3])
            
            print("Updated Loan History:",loan_record)
            ReturnResults.append("Updated Loan History:")
            ReturnResults.append(loan_record)

            
        # add each line back to .txt file after update.
        Updated_record=",".join(loan_record)
        logFile.writelines(Updated_record+"\n")
        BookReturned=True
    logFile.close()

    if BookReturned == True:
        print("Successfully returned book")
        ReturnResults.append("Successfully returned book")

    return ReturnResults



#Book Return can be tested via the GUI menu like booksearch.
