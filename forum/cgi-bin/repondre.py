#!/usr/bin/python3
import cgi 
import sqlite3

print("Content-type:text/html; charset=utf-8")
print()

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()

form = cgi.FieldStorage()
reponse = form.getvalue('reponse')
sujet= form.getvalue('id_sujet')
parent= form.getvalue('id_parent')

if len(reponse) == 0 :
    print("Un message vide ne peut pas être envoyé.") 
else:
    print("Commentaire envoyé !")
    cursor.execute('INSERT INTO message (contenu,id_auteur,id_sujet,id_parent,date_crea) VALUES (?,?,?,?,?)',(reponse,1,sujet,parent,"2026 06 07"))
    conn.commit()

conn.close()