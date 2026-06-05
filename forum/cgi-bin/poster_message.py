#!/usr/bin/python3
import cgi 
import sqlite3

print("Content-type:text/html; charset=utf-8")
print()

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
content = form.getvalue('contenu')
sujet= form.getvalue('id_sujet')

if len(content) == 0 :
    print("Un message vide ne peut pas être envoyé.") 
else:
    print("Commentaire envoyé !")
    cursor.execute('INSERT INTO message (contenu,id_auteur,id_sujet,id_parent,date_crea) VALUES (?,?,?,?,?)',(content,1,sujet,None,"2026 06 05"))
    conn.commit()

conn.close()