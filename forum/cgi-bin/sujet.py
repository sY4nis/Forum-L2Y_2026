#!/usr/bin/python3
import cgi 
import sqlite3

print("Content-type:text/html; charset=utf-8")
print()

form = cgi.FieldStorage()
id_sujet = form.getvalue('id')

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()

cursor.execute('SELECT sujets.titre FROM sujets WHERE sujets.id = ?', (id_sujet,))
id_title = cursor.fetchall()

cursor.execute('SELECT message.id, message.contenu,utilisateurs.pseudo FROM message JOIN utilisateurs ON message.id_auteur = utilisateurs.id WHERE message.id_sujet = ?', (id_sujet,))
id_content_pseudo = cursor.fetchall()

print(id_title[0][0])

for i in id_content_pseudo :
    print(f"<p><b>{i[2]}</b> : {i[1]}</p>")

print("<form action ='poster_message.py' method='POST'>")
print("<div>")
print("<label>Ajouter un commentaire:</label>")
print(f"<input type='hidden' name='id_sujet' value='{id_sujet}'/>")
print("<input type='text' name='contenu' placeholder='Votre message...'/>")
print("</div>")
print("<button type='submit'>Envoyer</button>")
print("</form>")
conn.close()
