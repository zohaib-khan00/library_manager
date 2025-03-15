import streamlit as st
import json

# Load & save library data

def load_library():
    try:
        with open("library.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_library(library):
    with open("library.json", 'w') as file:
        json.dump(library, file, indent=4)

    # initialize library
library = load_library()

st.title("📚Personal Library Manager")
menu = st.sidebar.radio("Select an option", ["View Library", "Add Book", "Remove Book", "Search Book", "Save & Exit"])
if menu == "View Library":   
    st.sidebar.title("Your Library")
    if library:
        st.table(library)
    else: 
        st.write("Your library is empty")

# Add book
elif menu == "Add Book":
    st.sidebar.title("Add a new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=2022, max_value=2100, step=1)
    pages = st.number_input("Pages", min_value=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")
    if st.button("Add Book"):
        library.append({"title": title, "author": author,"year": year,"pages": pages, "genre":genre, "read_status": read_status})
        save_library(library)
        st.success("Book added successfully")
        st.rerun()

# Remove book
elif menu == "Remove Book":
    st.sidebar.title("Remove a book")
    book_titles = [book["title"] for book in library]

    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_book]
            save_library(library)
            st.success("Book removed successfully")
            st.rerun()
    else:
        st.warning("Your library is empty")

# Search book
elif menu == "Search Book":
    st.sidebar.title("Search a Book")
    search_term = st.text_input("Enter Title or Author Name")
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No book found")

# save & exit
elif menu == "Save & Exit":
    save_library(library)
    st.success("Library saved successfully!")