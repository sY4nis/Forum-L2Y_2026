#!/usr/bin/python3
import cgi 
import sqlite3
import hashlib

print("Content-type:text/html; charset=utf-8")
print()

form = cgi.FieldStorage()
pseudo = form.getvalue('pseudo')
mdp = form.getvalue('mdp')
mdp_hash = hashlib.sha256(mdp.encode()).hexdigest()

conn = sqlite3.connect('forum.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM utilisateurs WHERE pseudo = ?',(pseudo,))
users_same_name = cursor.fetchall()

if len(users_same_name) > 0 :
    print("Le pseudo existe déjà")
elif len(pseudo) < 3 :
    print("Le pseudo choisie est trop court")
elif len(mdp) < 5 :
    print("Le mot de passe est trop court")
elif form.getvalue('confirmation') != mdp :
    print("Les mots de passe ne correspondent pas")
else:
    print("Inscription réussie")

    cursor.execute('INSERT INTO utilisateurs (pseudo, mdp, admin) VALUES (?, ?, ?)', (pseudo ,mdp_hash , 0))
    conn.commit()
    
conn.close()


