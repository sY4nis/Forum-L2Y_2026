#!/usr/bin/python3
import cgi 
import sqlite3

print("Content-type:text/html; charset=utf-8")
print()

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
titre = form.getvalue('titre')

if not titre or len(titre) < 1 :
    print("Le nom du sujet est vide.")
else:
    print("Création réussie !")

    cursor.execute('INSERT INTO sujets (titre, id_auteur, date_crea) VALUES (?, ?, ?)', (titre ,1 , "2026 06 05"))
    conn.commit()
    
conn.close()
