# BookKeeperProject
A python script for checking in/out books. Gives a terminal option menu that lets the user interact with library items.

## Input 
#### Terminal Option menu
1. Display Collection 
    - Displays the option of library items available based on the input file given
2. Check out materials
    - Lets the user check out a library item by entering in the book's call number
3. Quit
#### The input.txt file
- The first two row are parsed over 
- Col
    - Book
        1. B
        2. Call Number
        3. Title
        4. Author
        5. Genre
    - Periodical
        1. P
        2. Call Number
        3. Title
        4. Volume
        5. Issue
        6. Subject     
- See provided .txt file for an example


## Process
#### LA2main.py
- Main (Function)
    -  Uses a while loop to keep getting the input from the user, once quit is selected the while loop breaks, 
  and the program restarts
#### book_keeper.py
- Library items (Super Class)
    - Defines a library item
    - Determines checkout and due dates
    - Book (Sub Class)
    - Periodical (Sub Class)
- Controller (Class)
    - This class gives the main program access to library items in the input.txt
    - 'Controls' the user input
    - Parses the input.txt


## Output
#### Display Collection
- This menu selection will output the available info for each library item
    1. Book 
        1. Title
        2. Author
        3. Genre
        4. Call Number
        5. Check out status
    2. Periodical 
        1. Title
        2. Volume
        3. Issue
        4. Subject
        5. Check out status

#### Check out materials
- After entering the call number for a library item 
    1. If Item existed will display
       - all the data for the item
       - checked out date and due 
    
 
## Known Errors/Problems
- This program does not update the input.txt file so after the user quits all info is lost
