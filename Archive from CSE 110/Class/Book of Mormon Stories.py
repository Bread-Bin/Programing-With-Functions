greatest = 0
greatest_mormon = 0
mormon_book = ""
book_max = ""


with open("books_and_chapters.txt") as file:
    for line in file:
        book, chapter, scriptures = line.strip().split(":")
        chapter = int(chapter)
        
        if (scriptures == "Book of Mormon") and (chapter > greatest_mormon):
            greatest_mormon = chapter
            mormon_book = book
    
    print(f"G: {mormon_book} {greatest_mormon}")
        
        
    

        


#book_max_value = book_max.split(":")
#print(f'''Book with the most Chapters:
#Scripture: {book_max_value[2]}
#Book: {book_max_value[0]}
#Chapters: {book_max_value[1]}''')
