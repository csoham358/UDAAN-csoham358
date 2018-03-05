import pandas as pd
import numpy as np
import argparse


#Function to Add new Book
def add_book(file_loc, book_id, book_name, book_author):
    df=pd.read_csv(file_loc, delimiter=',', header=None)
    df=df.drop(df.columns[[0]], axis=1)
    df.columns=['Sno', 'id', 'name', 'author', 'std_id', 'date']
    

    sno=np.max(df.Sno)+1
    df.loc[-1] = [sno, book_id, book_name, book_author, 0, 0]
    
    df.index=df.index+1
    df=df.sort_index()
    df.to_csv('books.csv', sep=',')
    print(df.head())

#Function To Borrow Books
def borrow_book(file_loc, stud_id, date, book_name=None, book_author=None, book_id=None):

    df=pd.read_csv(file_loc, delimiter=',', header=None)
    df=df.drop(df.columns[[0]], axis=1)
    
    df.columns=['Sno', 'id', 'name', 'author', 'std_id', 'date']
    
    if book_id:
        df.loc[df.id == book_id, ['std_id']]=stud_id
        df.loc[df.id == book_id, ['date']]=date
    
    if book_name:
        df.loc[df.name == book_name, ['std_id']]=stud_id
        df.loc[df.name == book_name, ['date']]=date
    
    if book_author:
        df.loc[df.author == book_author, ['std_id']]=stud_id
        df.loc[df.author == book_author, ['date']]=date

    df.to_csv('books.csv', sep=',')

#Function to check due date
def check_duedate(file_loc, book_id, due_date):
    df=pd.read_csv(file_loc, delimiter=',', header=None)
    df=df.drop(df.columns[[0]], axis=1)
    
    df.columns=['Sno', 'id', 'name', 'author', 'std_id', 'date']

    yo=np.where(df['std_id'] == book_id)
    
    df1=df.iloc[yo]
    if (df1.date==due_date).bool():
        print("Book is Due")

if __name__ == '__main__':

    parser=argparse.ArgumentParser(description='Description of your program')

    parser.add_argument('-type','--type', help='1 to add new book to library; 2 to Borrow/reserve book; 3 to check due date', required=True)
    parser.add_argument('-name', '--name', help='Enter name of new book to add')
    parser.add_argument('-id', '--id', help='Enter id of new book to add/reserve/check')
    parser.add_argument('-author', '--author', help='Enter author of new book to add or search')
    parser.add_argument('-std', '--std', help='Enter student id of student who is borrowing book')
    parser.add_argument('-duedate', '--duedate', help='Enter due date of book to check or reserve')
    results = parser.parse_args()
    
    
    if results.type == '3':
        book_id=results.id
        due_date=results.duedate
        check_duedate(file_loc='books.csv', book_id='5', due_date='10')
    
    if results.type == '1':
        add_book(file_loc='books.csv', book_id='32', book_author='Nietzsche', book_name='Thus Spoke Zarathustra')
    if results.type =='2':
        borrow_book(file_loc='books.csv', stud_id=5, date=10, book_id='20')