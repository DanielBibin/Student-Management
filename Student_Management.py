import register, modify, delete, display, streamlit as st, sqlite3 as sq, os, keyboard, time
from streamlit_option_menu import option_menu

conn = sq.connect("Student_Management.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Student(Adno TEXT, Name TEXT, class_div TEXT)")
conn.commit()
st.markdown("<h1 style = 'text_align: center;' >STUDENT MANAGEMENT SYSTEM</h1>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu("Main Menu", ["Register", "Modify", "Delete", "Display"], default_index=0)

if selected == 'Register':
    Student_1 = register.Register()
elif selected == 'Modify':
    Student_1 = modify.Modify()
elif selected == 'Delete':
    Student_1 = delete.Delete()
elif selected == 'Display':
    Student_1 = display.Display()

cursor.execute("SELECT Adno FROM Student;")
AdmNo = cursor.fetchall()
Ano = []
for i in range(len(AdmNo)):
    Ano.append(AdmNo[i][0])
for i in Ano:
    cnt = Ano.count(i)
    if cnt>1:
        cursor.execute("SELECT * FROM Student WHERE Adno=?", (i,))
        dup = cursor.fetchall()
        Adno = dup[0][0]
        Name = dup[0][1]
        class_div = dup[0][2]
        cursor.execute("DELETE FROM Student WHERE Adno = ?", (i,))
        conn.commit()
        cursor.execute("INSERT INTO Student VALUES(?, ?, ?)", (Adno, Name, class_div))
        conn.commit()
        
conn.close()
