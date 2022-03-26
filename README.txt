HOW TO USE THE PROGRAMS FUNCTIONS VIA GUI MENU:

  -Book Search: Input a book title and then press "SEARCH BOOK" button. (e.g book1) 

  -Check out Book: Input member ID, book ID and a date then press "CHECKOUT BOOK".

  -Return Book: Input a book ID and then press "RETURN BOOK".

  -Weeding Library Books: Press the "WEED LIBRARY" button.

  Note: All of these functions can still work without correct or missing inputs.

EXPLAINATIONS OF THE FUNCTIONS NOT ADDRESSED IN THE SPECIFICATION:

  -Return Dates: My return date is set about a month after the checkout date was made. 
                  (e.g check out date 16 12 2020 so then the return date is 16 1 2021)

  -Weeding Criteria: In the weeding process I decided to take in two factors: the book's condition 
                     and the book's total withdrawn count.
                     
                     A book is weeded if and only if a book's condition is both "POOR" and below 
                     the minimal threshold of withdrawals. (This is represented as a red line on the 
                     bar chart and is set to 5.) 


BEST PART OF THE PROGRAM:

   -Bar chart animates check out updates: As the bar chart is embedded in the gui, it 
    can't leave the menu. Therefore when you go through a successful book checkout again and click
    the weeding button again, the bar for that book id will update. This will keep on going as the more
    book check outs are processed. You will also see how this affects the low withdraw list found in 
    output box of the program on the weeding function.                    

DEPRECATION WARNING ON MATPLOTLIB:

   -Deprecation warning for Matplotlib can be ignored as it does not disturb the program's processes.
    This is caused due to the red line implemented in the bar chart. I decided not to remove the 
    dotted red line because it gives more information than without it.

