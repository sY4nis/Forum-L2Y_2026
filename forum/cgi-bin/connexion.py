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

cursor.execute('SELECT * FROM utilisateurs WHERE pseudo = ? AND mdp = ? ',(pseudo,mdp_hash))
users_same_name = cursor.fetchall()

if len(users_same_name) == 0 :
    print("Le mot de passe ou le nom d'utilisateur est incorrecte, veuillez réssayer.")
else:
    print("Connexion réussie, veuillez patienter.")

conn.close()