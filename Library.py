# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

while True:
    print("Library Management System")
    print("==========================")
    print("1. Print books info.")
    print("2. Search a book.")
    print("3. Add new book.")
    print("4. Remove a book.")
    print("5. Borrow a book.")
    print("6. Return a book.")
    print("7. Exit")
    print("==========================")
    choice = input("Enter your choice: ")
    #Print books info
    if choice == "1":
        books = open("booksinfo.txt")
        count = 0 #a variable to store the number of total books
        book_info = [] #here, I'm going to store each line in the file
        
        print("-----------------------------------")
        
        for j in books:
            strip_j = j.rstrip() #deleting \n
            book_info = strip_j.split(",") #turning every line to a list
            print("Serial number: ", book_info[0])
            print("Title: ", book_info[1])
            print("Number of authors:", len(book_info[2].split(":"))) #turning the authors to another list
            print("Price:", book_info[3])
            print("Total copies:", int(book_info[4]) + int(book_info[5])) 
            print("-------------------------------------")
            count = count + 1
        print("Total Books: ", count)
        print("-----------------------------------------")
        books.close()
    #Search a book
    elif choice == "2":
         books = open("booksinfo.txt")
         search = input("Enter (t) to search by title or (a) to search by the author name:")
         #The following loop is pretty much the same as the previous one
         book_info = []
         if search == "t":
            title = input("Enter the book title: ")
            count = 0 #a variable to keep track of matched records
            for i in books:
                 strip_i = i.rstrip()
                 book_info = strip_i.split(",")
                 if title == book_info[1]:
                     count = count + 1
                     print("Matched records: ")
                     print("Serial number:", book_info[0])
                     print("Title: ", book_info[1])
                     authors = book_info[2].split(":") #a list of authors to print them independently
                     print("authors: \n")
                     for j in authors:
                         print("    -" + j + "\n")
                     print("Price: ", book_info[2])
                     print("Copies in library: ", book_info[3])
                     print("Borrowed copies: ", book_info[4])
            if count == 0:
                 print("There is no book that has this title.")
                 
         elif search == "a":
             author = input("Enter the author name: ")
             count = 0
             for i in books:
                 strip_i = i.rstrip()
                 book_info = strip_i.split(",")
                 authors = book_info[2].split(":") #a list of authors to compare the to the input
                 if author == authors[0] or author == authors[1]:
                     count = count + 1 
                     print("Matched records: ")
                     print("Serial number:", book_info[0])
                     print("Title: ", book_info[1])
                     print("authors: \n","-",authors[0],"\n","-",authors[1])
                     print("Price: ", book_info[2])
                     print("Copies in library: ", book_info[3])
                     print("Borrowed copies: ", book_info[4])
             if count == 0:
                 print("There is no author that has this name.")
                                  
         else:
                print("Enter a valid input!")
         books.close()
    #Add new book
    elif choice == "3":
        books = open("booksinfo.txt", "a") #open file in append mode
        serial_number = input("Enter the serial number of the book: ")
        book_title = input("Enter the book title: ")
        not_finished = True
        count = 0 #a variable to count the number of authors
        authors_group = [] #a list to store authors' names
        while not_finished:
            count = count + 1
            author_name = input("Enter the name of author " + str(count) + ": ")
            if author_name != "q":
                authors_group.append(author_name)
            elif author_name == "q":
                not_finished = False
        book_price = input("Enter book price: ")
        number_of_copies= input("Enter the number of the book copies: ")
        
        #The following if and try\except statements check if the input entered previously
        #by the user are correct.
        
        all_correct = True 
        
        if len(serial_number) < 5 or len(serial_number) > 5:
            all_correct = False
            print("The serial number must contain 5 digits only.")
        
        with open("booksinfo.txt") as books_readable:
           for line in books_readable:
               if line.find(serial_number) != -1:
                  all_correct = False
                  print("Serial number is already used.")
        
    
        try:
            int(serial_number)
        except:
            all_correct = False
            print("The serial number must be a valid integer.")

                   
        
        if book_title == "":
            all_correct = False
            print("Book title must not be empty.")
            
        for i in authors_group:
            if i == "":
                all_correct = False
                print("The name of author must not be empty.")
        
        if book_price == "":
            all_correct = False
            print("Book price must not be empty")
        
    
        
        try:
            float(book_price)
        except:
            all_correct = False
            print("The book price  must be a valid float.")
        
        if number_of_copies == "":
            all_correct = False
            print("Number of copies must not be empty.")
            
       
        
        try:
            int(number_of_copies)
        except:
            all_correct = False
            print("Number of copies must be a valid integer.")
            
            
        #The following code removes brackets an quoatations from
        #the auothers_groups list to make it look like a regular string
        #then, the commas are replaced by colons.
        authors_group_brackets_removed1 = str(authors_group).replace("[", "")
        authors_group_brackets_removed2 = authors_group_brackets_removed1.replace("]", "")
        authors_group_quote_removed = authors_group_brackets_removed2.replace("\'", "")
        final_authors_str = authors_group_quote_removed.replace("," , ":")

       
        
        if all_correct == True:
           books.write("\n" + serial_number+","+book_title+","+final_authors_str+","+book_price+","+number_of_copies +","+ "0"+"\n")
        
        books.close()
    #Remove a book
    elif choice == "4":
        serial_number = input("Enter the serial number to remove: ")
        book_to_be_deleted = [] # a list to store the book to be deleted
        lines = "" # a variable to store the file content
        with open('booksinfo.txt', 'r') as rf:
               lines = rf.readlines()
 
        for line in lines:
            book_to_be_deleted = line.split(",")
            #here we check if the book contains the serial number were the find method
            #does not return -1, we also make sure that the book is not borrowed.
            if line.find(serial_number) != -1 and int(book_to_be_deleted[5]) == 0:
                print("Serial number: ", book_to_be_deleted[0])
                print("Title: ", book_to_be_deleted[1])
                print("Number of authors:", len(book_to_be_deleted[2].split(":"))) #turning the authors to another list
                print("Price:", book_to_be_deleted[3])
                print("Total copies:", int(book_to_be_deleted[4]) + int(book_to_be_deleted[5])) 
                print("-------------------------------------")
                confirm = input("Deleting the book... are you sure? (y/n) ")
                if confirm == "y":
                    #here we make another for loop thru the file content again, to write the
                    #lines that does not contain the serial number to another new file
                    with open('booksinfo.txt', 'w') as wf:
                     for i in lines:
                        if i.find(serial_number) == -1:
                                wf.write(i)
                                print("The book was successfully removed.")
                elif confirm == "n":
                    print("Operation is cancelled.")
                    break
                else:
                    print("Please... enter a valid input.")
            else:
                print("The book is not found, or the book is borrowed.")
    #Borrow a book
    elif choice == "5":
        #firstly, we check if the serial number has the right length or not.
        serial_number = input("Enter the serial number of the book: ")
        if len(serial_number) < 5 or len(serial_number) > 5:
                   print("Serial number should be 5 digits.")
                   continue
               
        ID = input("Enter user ID: ")
        books = open("booksinfo.txt")
        borrowed = open("borrowedinfo.txt", "r")
        lines = books.readlines()
        
        #We search in booksinfo.txt to see if the book exists
        if str(lines).find(serial_number) == -1:
            print("No matched serial number.")  
            continue
        
        lines_of_borrowed = borrowed.readlines()
        borrowed.close() #we keep the file closed for the time being.

        
        for line in lines:
            line.rstrip()
            line_list = line.split(",")
            serial_ID =  serial_number+","+ID
            if serial_number == line_list[0]:
                
                #if the serial number exists for any of the books (lines)
                #we see if the conditions are met or not as follows.
                
                if int(line_list[4]) == 0:
                   print("No available copies in the library.")
                   break
                   
               
                if str(lines_of_borrowed).count(ID.strip()) == 3:
                   print("User can not borrow more than 3 books.")
                   break
                   
               
                if str(lines_of_borrowed).find(serial_ID.strip()) != -1:
                   print("User already borrowed a copy of the book.")
                   break
                   
                #After checking all the conditions, we open borroedinfo.txt
                #to add a new record.
                with open("borrowedinfo.txt", "a+") as toBorrow:
                    toBorrow.writelines(serial_number+","+ID+"\n")
                    print("Successfully borrowed.")
                    books.close() #after we done reading the file, we close it.
                    #here, we take the line that contains the borrowed book
                    #and we increase the number of borrowed copies.
                    #then we transform it back to a string to store it 
                    #in booksinfo.txt
                    line_list[5] = int(line_list[5]) + 1
                    line_list[4] = int(line_list[4]) - 1
                    line_list_str = str(line_list).replace("[", "")
                    line_list_str2 = line_list_str.replace("]", "")
                    line_list_str3 = line_list_str2.replace("\'", "")
                    line_list_str4 = line_list_str3.replace(" ", "")
                    with open("booksinfo.txt", "w") as toRewrite:
                        for line in lines:
                            #here we write all the books except the borrowed one
                            #then we append the borrowed book with the number of borrowed
                            #books increased.
                            if line.find(serial_number) == -1:
                                toRewrite.writelines(line)
                    with open("booksinfo.txt", "a") as toIncrease:
                        toIncrease.writelines(line_list_str4)
                                
                    
        books.close()
        
    #Return a book
    elif choice == "6":
        #firstly, we check if the serial number has the right length or not.
        serial_number = input("Enter book serial number to return: ")  
        if len(serial_number) < 5 or len(serial_number) > 5:
                   print("Serial number should be 5 digits.")
                   continue
        
        ID = input("Enter user ID: ")
        books = open("booksinfo.txt")
        book_lines = books.readlines()
        borrowed_books = open("borrowedinfo.txt", "r")
        lines = borrowed_books.readlines()
        
        if str(lines).count(serial_number+","+ID) == 0:
            print("No matched record found in borrowedInfo.txt")
        else:
            #we rewrite the booksinfo.txt by writing the records again
            #with the exception of the record that contains the searched serail number and ID
            for line in lines:
                 line = line.rstrip()
                 if line.find(serial_number+","+ID) == -1:
                     borrowed_books.close()
                     with open("borrowedinfo.txt", "w") as rewrite:
                          for line in lines:
                              if line.find(serial_number+","+ID) == -1:
                                  rewrite.write(line)
            print("The book was successfully returned.")
            
            #here, we append the recored that has the returned book to the booksinfo.txt
            #After rwriting the file with the exception of the recored that has the returned book
            
           
            
            with open("booksinfo.txt", "w") as rewrite_books:
              for line in book_lines: 
                    if line.find(serial_number) == -1:
                        rewrite_books.writelines(line)
            
            
            with open("booksinfo.txt", "a") as append_books:
              for book in book_lines: 
                    book = book.rstrip()
                    book_list = book.split(",")
                    if serial_number == book_list[0]:
                        book_list[5] = int(book_list[5]) - 1
                        book_list[4] = int(book_list[4]) + 1
                        book_list_str = str(book_list).replace("[", "")
                        book_list_str2 = book_list_str.replace("]", "")
                        book_list_str3 = book_list_str2.replace("\'", "")
                        book_list_str4 = book_list_str3.replace(" ", "")
                        append_books.writelines("\n" + book_list_str4)
                        
            
    elif choice == "7":
        print("Existing the application...")
        #here we use the sys library to be able to exit the library.
        sys.exit()
    else:
      print("Please, enter a valid input.")
      print("----------------------------------------------")
        
                                    
                                
                                
                        
                        
                
            
      
                
            
        
        
        
            
                
        
        
        
        
            
        
                   
                        
                
        
        
        

            
            
        
        
             
             
              
                    
                    
                 
                 
                 
                 
             
        
        
      


            
        
        

    