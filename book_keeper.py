from datetime import datetime, timedelta


class LibraryItem:
    # Initializer method – Updates the call number, checkedOut, dateCheckedOut and dueDate fields.
    def __init__(self, checkout_type, call_num):
        self.__call_num = call_num
        self.__checkout_type = checkout_type
        self.__checked_out = False
        self.__date_checked_out = 'N/A'
        self.__date_due = 'N/A'

    # Sets the boolean value checkedOut to true, and
    # initializes the dateChecked out attribute (with
    # the current date – date on which item was checked out).
    def check_out(self):
        """
        Determines whether the library has been checkout, the items due date, and checkout date

        :return: checked_out, date_checked_out, due_date
        """
        self.__checked_out = True
        if self.__checkout_type == 'B':
            self.__date_checked_out = str(datetime.today())
            self.__date_due = str(datetime.today() + timedelta(days=21))
        elif self.__checkout_type == 'P':
            self.__date_checked_out = str(datetime.today())
            self.__date_due = str(datetime.today() + timedelta(days=7))
        else:
            self.__checked_out = False

    # Getter for the call number of this object.
    # @return - the callNumber
    def get_call_number(self):
        return self.__call_num

    # Returns true or false depending on if this item has been checked out.
    # @return - the boolean value for isCheckedOut
    def is_checked_out(self):
        return self.__checked_out

    # Returns the date this item was checked out.
    # @return - the date the item was checked out
    def get_date_checked_out(self):
        return self.__date_checked_out

    # Returns the date this item is due to be returned.
    # @return - the due date
    def get_date_due(self):
        return self.__date_due

    # Sets the dateDue to the parameter received.
    # @parameter dateDue - the new due date
    def set_date_due(self, due_date):
        self.__date_due = due_date


class Book(LibraryItem):
    def __init__(self, checkout_type, call_num, title, author, genre):

        LibraryItem.__init__(self, checkout_type, call_num)
        self.__author = author
        self.__genre = genre
        self.__title = title

    # Generates a string with the details of the library item
    # whose call number has been input by the user (see example output)
    # and returns that string.
    # If the user wants to check out the library item, the string to be
    # returned also includes information that the item has been checked out,
    # the date it was checked out, and the due date by which the item should be returned.
    # @return – The generated string.
    def __str__(self):
        """
        creates a string for a book object

        :return: book_str
        """
        book_str = 'Book Title: ' + self.__title + '\n' + 'Author: ' + self.__author + '\n' + 'Genre: ' \
                   + self.__genre + '\n' + 'Call Number: ' + self.get_call_number() + '\n'
        if self.is_checked_out():
            book_str = book_str + 'Checked out: YES' + '\n' + 'Date out: ' + self.get_date_checked_out() + '\n' \
                       + 'Date Due: ' + self.get_date_due() + '\n'
        else:
            book_str = book_str + 'Checked out: NO'
        return book_str


class Periodical(LibraryItem):
    def __init__(self, checkout_type, call_num, title, volume, issue, subject):
        LibraryItem.__init__(self, checkout_type, call_num)
        self.__volume = volume
        self.__issue = issue
        self.__subject = subject
        self.__title = title

    def __str__(self):
        """
        creates a string for a periodical object

        :return: periodical_str
        """
        periodical_str = 'Periodical Title: ' + self.__title + '\n' + 'Volume: ' + self.__volume + '\n' + 'Issue: ' \
                         + self.__issue + '\n' + 'Subject: ' + self.__subject + '\n' + 'Call Number: '\
                         + self.get_call_number() + '\n'
        if self.is_checked_out():
            periodical_str = periodical_str + 'Checked out: YES' + '\n' + 'Date out: ' + self.get_date_checked_out() \
                             + '\n' + 'Date Due: ' + self.get_date_due() + '\n'
        else:
            periodical_str = periodical_str + 'Checked out: NO'
        return periodical_str


class Controller:
    # Initializer method: - creates an empty list of library items. This will be used to store the library items in the
    # input file.
    def __init__(self):
        self.__list_library_items = []

    # Displays the menu options to the user.
    def show_menu(self):
        print('-----------Menu-----------')
        print('1) Display collection')
        print('2) Check out materials')
        print('3) Quit')
        print('--------------------------')

    # Displays the collection of library items on the screen
    def display_collection(self):
        for library_item in self.__list_library_items:
            print(library_item)
            print()
            print()

    # Searches in the list of library items
    # for the item with the call number received as a parameter.
    # @parameter callNum - The call number of the item requested by the user (of type “string”)
    # @return - The requested item (if found)
    def find_item(self, call_num):
        """
        Looks for the library item for the given call number

        :param call_num: the only parameter passed to the function

        :return: material, an LibraryItem object
        """
        for material in self.__list_library_items:
            if material.get_call_number() == call_num:
                return material

        return 'Not Found'

    # Requests for the call number from the user, uses the findItem()
    # method to check if that item exists in the library, and if it does
    # calls the checkOut() method for that item and prints out the item
    # that has been checked out.
    def check_out_materials(self, user_input):
        item_exist = self.find_item(user_input)
        if item_exist == 'Not Found':
            print(user_input, 'was not found')
        else:
            item_exist.check_out()
            print(item_exist)

    # Reads data from the input file and stores the items in the
    # appropriate array.
    # @parameter filename - The name of the input file (of type “string”)
    def read_input(self, file_name):
        library = open(file_name, mode='r')
        with library:
            library.readline()
            library.readline()
            for item in library:
                item = item.rstrip('\n')
                if item[0] == 'B':
                    checkout_type, call_num, title, author, genre = item.split(',')
                    item_instance = Book(checkout_type, call_num, title, author, genre)
                elif item[0] == 'P':
                    checkout_type, call_num, title, volume, issue, subject = item.split(',')
                    item_instance = Periodical(checkout_type, call_num, title, volume, issue, subject)

                self.__list_library_items.append(item_instance)
