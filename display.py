import streamlit as st, sqlite3 as sq
class Display:
    def __init__(self):
        conn = sq.connect("Student_Management.db")#connecting to sqlite3 database
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student;")#accepting values of tables in database
        conn.commit()
        st.header("Display")

        st.dataframe(cursor)#displaying in streamlit in table form
        
        conn.close()#closing connection with database
