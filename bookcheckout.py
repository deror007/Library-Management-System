'''
Book Checkout allows the librarian to confirm a book checkout. It does so
by validating book and member id's.Given a correct date it can give the return
date which is a month after. Results of this will be displayed in the
interpreter GUI output box. (Also within GUI bar chart of the weed library)
'''
def validateMemberID(MemberID):

    if MemberID.isnumeric()==True and len(MemberID)== 4:
        return True
    else:
        return False

def checkBookID(BookID):

    if BookID.isnumeric()==True:
        return True
    else:
        return False

def IDcheck(MemberID,BookID):
    
    if validateMemberID(MemberID) == True and checkBookID(BookID)==True:
        print("VALID: Member ID & Book ID are provided.")
        return True

    else:

        return False

def Available(BookID,DatabaseList): #Check wanted book is available
                            
    checker=False
    for bookinfo in DatabaseList:
        bookinfo=bookinfo.replace("\n","")
        BookEntry=bookinfo.split(",")

        if "0000" == BookEntry[5] and BookID == BookEntry[0]:
            checker=True
            print("Book is Available")

            return True
        
    if checker == False:

        return False
    
def getCheckOutDate(day,month,year):
    if month != None and month != None and month.isnumeric()==True and year.isnumeric()==True:
            CheckoutDate=(day+"/"+month+"/"+year)
            return CheckoutDate
    else:
        return("No Check-Out Date")



def getReturnDate(day,month,year):
    if month != None and month != None and month.isnumeric()==True and year.isnumeric()==True:
        nextMonth=str(int(month)+1)
        if nextMonth=="13":
            January="1"
            nextYear=str(int(year)+1)
            ReturnDate=(day+"/"+January+"/"+nextYear)
            return ReturnDate
        else:
            ReturnDate=(day+"/"+nextMonth+"/"+year)
            return ReturnDate
    else:
        return("No Return Date")

#Updates the number of withdrawns for a book, this results in change for
#weeding graph. THE GRAPH WILL UPDATE AND ANIMATE CHANGE ON BAR CHART.
def newWithdrawnNo(record):
    WithdrawnNo=str(int(record[3])+1)
    return WithdrawnNo

        
def withdrawBook(MemberID,BookID,DatabaseList,LogFileList,Day,Month,Year):
    ReturnResults = []
    ReturnResults.append("---------CHECKOUT A BOOK:---------")
    
    BookWithdrawn = False


    #updated availability of given ID's in Database.txt
    dataFile = open("database.txt","w")
    for db_record in DatabaseList: 
        db_record=db_record.replace("\n","")
        db_record=db_record.split(",")

        if BookID == db_record[0]:
            db_record.insert(5,MemberID)
            del(db_record[6])
            
            print("Updated Book Details:",db_record)
            ReturnResults.append("Updated Book Details:")
            ReturnResults.append(db_record)
            
        # add each line back to .txt file after update.
        Updated_record=",".join(db_record)
        dataFile.writelines(Updated_record+"\n")
    dataFile.close()


    #update loan history of given ID's in Logfile.txt
    logFile = open("logfile.txt","w")
    for loan_record in LogFileList: 
        loan_record=loan_record.replace("\n","")
        loan_record=loan_record.split(",")

        if BookID == loan_record[0]:
            loan_record.insert(1,getCheckOutDate(Day,Month,Year))
            del(loan_record[2])
            loan_record.insert(2,getReturnDate(Day,Month,Year))
            del(loan_record[3])
            loan_record.insert(3,newWithdrawnNo(loan_record))
            del(loan_record[4])            

            print("Updated Loan History:",loan_record)
            ReturnResults.append("Updated Loan History:")
            ReturnResults.append(loan_record)            
            
        # add each line back to .txt file after update.
        Updated_record=",".join(loan_record)
        logFile.writelines(Updated_record+"\n")
        BookWithdrawn=True
    logFile.close()

    if BookWithdrawn == True:
        print("Successfully withdrawn book")
        ReturnResults.append("Successfully withdrawn book")

    return ReturnResults



#bookcheckout.py input test code.


if __name__=="__main__":
    #Test different member ID inputs 
    print(validateMemberID("7654"))
    print(validateMemberID("ergkhu"))
    print(validateMemberID("123353"))
    print(validateMemberID(" "))
    #Test different inputs for book ID
    print(checkBookID("10"))
    print(checkBookID("aaasdn"))
    print(checkBookID(" "))
    #Test different inputs of memberId and bookID.
    print(IDcheck("7654","10"))
    print(IDcheck("7654"," "))
    print(IDcheck("7fdgfdg","10"))
    #Test different inputs of day month year.
    print(getCheckOutDate("1","11","2020"))
    print(getCheckOutDate("1d","1a","202d0"))
    #Test if return date would be a month later.
    print(getReturnDate("1","12","2020"))
    print(getReturnDate("17","5","2020"))
    print(getReturnDate("1","12"," "))
    
