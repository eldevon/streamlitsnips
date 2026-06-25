import streamlit as st
import sqlite3


def init_db():
    conn = sqlite3.connect("names.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS people \
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    conn.commit()
    conn.close()

def insert_name(name): 
    conn = sqlite3.connect("names.db")
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO people (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()


st.title("Add Name to Database")

init_db()

name = st.text_input("Enter a name: ")

# Save names
if st.button("Save"): 
    if name.strip(): 
        insert_name(name.strip()) 
        st.success("Name saved successfully.")

# Get all names
def get_all_names(): 
    conn = sqlite3.connect("names.db") 
    cursor = conn.cursor() 
    cursor.execute("SELECT id, name FROM people") 
    rows = cursor.fetchall() 
    conn.close() 
    return rows

# Deletes name from table
def delete_name(id): 
    conn = sqlite3.connect("names.db") 
    cursor = conn.cursor() 
    cursor.execute("DELETE FROM people WHERE id = ?", (id,)) 
    conn.commit() 
    conn.close()

# Changes title to Delete	
st.title("Delete a Name")
names = get_all_names()
id_list = [row[0] for row in names]

# Creates a select option for deleting name
selected_id = st.selectbox("Select ID to delete:", id_list)
if st.button("Delete"):
	delete_name(selected_id)
	st.success("Deleted successfully.")

# Updating a row
def update_name(id, new_name): 
    conn = sqlite3.connect("names.db") 
    cursor = conn.cursor() 
    cursor.execute("UPDATE people SET name = ? WHERE id = ?", 
    (new_name, id)) 
    conn.commit() 
    conn.close()

# Change title for updating	
st.title("Update a Name")
names = get_all_names()
id_list = [row[0] for row in names]

# Select box for updating 
selected_id = st.selectbox("Select ID to update:", id_list)
new_name = st.text_input("Enter new name:")
if st.button("Update"): 
    if new_name.strip(): 
        update_name(selected_id, new_name.strip()) 
        st.success("Updated successfully.")

# Changes title to show saved names
st.title("View Saved Names")
names = get_all_names()
# Displays the names in a row with id and name
st.subheader("Name List")
for row in names: 
    st.write(f"{row[0]}. {row[1]}")