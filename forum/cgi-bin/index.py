#!/usr/bin/python3
import cgi 
import sqlite3

print("Content-type:text/html; charset=utf-8")
print()

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()


cursor.execute('SELECT sujets.titre, utilisateurs.pseudo FROM sujets JOIN utilisateurs ON sujets.id_auteur = utilisateurs.id')
title_pseudo = cursor.fetchall()
print("<ul>")
for i in title_pseudo :
    print(f"<li><a href = '#'>{i[0]} par : {i[1]} </a></li>")
print("</ul>")

print("Lancer un nouveau sujet")
print("<form action ='sujet.py' method='POST'>")
print("<div>")
print("<label>Titre du sujet:</label>")
print("<input type='text' name='titre' />")
print("</div>")
print("<button type='submit'>Créer</button>")
print("</form>")
conn.close()
