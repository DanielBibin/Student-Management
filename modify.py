import streamlit as st, sqlite3 as sq
cnt = 0
class Modify:
    def __init__(self):
        st.header("Modification")
        Modification_Form = st.form("Modification Form")#creating streamlit form
        def Modification():
            conn = sq.connect("Student_Management.db")#connecting to sqlite3 database
            cursor = conn.cursor()
            global cnt
            if len(Adno) > 0 and len(Name) > 0 and len(class_div) > 0:#checking if all fields have been inputted
                cursor.execute("SELECT Adno FROM Student;")#accepting all values of column 'adno'
                AdmNo = cursor.fetchall()
                Ano = []
                for i in range(len(AdmNo)):
                    Ano.append(AdmNo[i][0])
                if Adno in Ano:#checking if the admission number already exists
                    cnt=0
                    cursor.execute("UPDATE Student SET Name = ?, class_div = ? WHERE Adno = ?", (Name, class_div, Adno))#modifying with values supplied by the user to the database
                    conn.commit()#commiting the changes to the database
                    Modification_Form.markdown("Successfully Modified")
                else:
                    cnt = 0
                    Modification_Form.warning("Students Record Does Not Exist")#putting out a warning that the student records do not exist
            conn.close()#closing connection with the database
            
        with Modification_Form:#using the streamlit form
            Adno = st.text_input("Enter Admission Number Of Student Record To Be Modified:")#text input for the admission number of the student record to be modified
            Name = st.text_input("Enter New Name:")#text input for the new name
            class_div = st.text_input("Enter New Class And Division:")#text input for the new class and division
            col1, col2, col3, col4, col5 = st.columns(5)
            with col3:
                st.form_submit_button("Modify", on_click=Modification())#creating form submit button
    
