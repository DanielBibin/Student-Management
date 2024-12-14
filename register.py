import streamlit as st, sqlite3 as sq
cnt = 0
class Register:
    def __init__(self):
        st.header("Registration")
        Registeration_Form = st.form("Registeration Form")#creating the streamlit form
        def Registeration():
            conn = sq.connect("Student_Management.db")#creating connection with the sqlite3 database
            cursor = conn.cursor()
            global cnt
            if len(Adno) > 0 and len(Name) > 0 and len(class_div) > 0:#checking if all values have been inputted
                cursor.execute("SELECT Adno FROM Student;")#accepting all values from column 'adno' from database
                AdmNo = cursor.fetchall()
                Ano = []
                for i in range(len(AdmNo)):
                    Ano.append(AdmNo[i][0])
                if Adno not in Ano:#checking if adno is already present in the database
                    cnt=0
                    cursor.execute("INSERT INTO Student VALUES(?, ?, ?)", (Adno, Name, class_div))#inserting the values provided by the user into the database
                    conn.commit()#commiting changes to the database
                    Registration_Form.markdown("Successfully Registered")
                else:
                    cnt = 0
                    Registeration_Form.warning("Students Record Already Exist")#putting out a warning if the database already exists
            conn.close()#closing the connection with the database


        with Registeration_Form:#using the form
            Adno = st.text_input("Enter Admission Number of New Student:")#text input for admission number of the new student
            Name = st.text_input("Enter Name of New Student:")#text input for the name of the new student
            class_div = st.text_input("Enter Class And Division Of New Student:")#text input for the class and division of the new student
            col1, col2, col3, col4, col5 = st.columns(5)
            with col3:
                st.form_submit_button("Register", on_click=Registeration())#creating strealit form submit button
                
        
    
