import streamlit as st, sqlite3 as sq
cnt = 0
class Delete:
    def __init__(self):
        st.header("Deletion") 
        global Deletion_Form
        Deletion_Form = st.form("Deletion Form")#creating streamlit form
        with Deletion_Form:
            Adno = st.text_input("Enter Admission Number Of Student Record To Be Deleted:")#text input to input admission number to be deleted
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])#creating columns for better button placing 
            with col3:#using column 3
                submit_button = st.form_submit_button("Delete")#form submit button
            if submit_button:
                conn = sq.connect("Student_Management.db")
                cursor = conn.cursor()
                global cnt
                if len(Adno) > 0:#checking if adno is empty
                    cursor.execute("SELECT Adno FROM Student;")#accepting all values from column 'adno' from database
                    AdmNo = cursor.fetchall()
                    Ano = []
                    for i in range(len(AdmNo)):
                        Ano.append(AdmNo[i][0])
                    if Adno in Ano:#checking if Adno is already present in the database
                        cnt=0
                        cursor.execute("DELETE FROM Student WHERE Adno = ?", (Adno,))#executing sqlite3 command for deletion of values
                        conn.commit()#commiting changes to database
                        Deletion_Form.markdown("Successfully Deleted")
                    else:
                        cnt=0
                        Deletion_Form.warning("Student Records Does Not Exist")
                conn.close()#closing connection with database
        
