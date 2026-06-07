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

cursor.execute('SELECT message.id, message.contenu,utilisateurs.pseudo, message.id_parent FROM message JOIN utilisateurs ON message.id_auteur = utilisateurs.id WHERE message.id_sujet = ?', (id_sujet,))
id_content_pseudo_parent = cursor.fetchall()

print(id_title[0][0])

def affiche_reponse(id_message, cursor, id_sujet):
    cursor.execute('SELECT message.id, message.contenu, utilisateurs.pseudo FROM message JOIN utilisateurs ON message.id_auteur = utilisateurs.id WHERE message.id_parent = ?', (id_message,))
    id_content_pseudo= cursor.fetchall()
    
    if len(id_content_pseudo) > 0:
        print("<ul>")
        for r in id_content_pseudo:
            print("<li>")
            print(f"<p><b>{r[2]}</b> : {r[1]}</p>")
            print("<form action ='repondre.py' method='POST'>")
            print("<div>")
            print("<label>Répondre:</label>")
            print(f"<input type='hidden' name='id_parent' value='{r[0]}'/>")
            print(f"<input type='hidden' name='id_sujet' value='{id_sujet}'/>")
            print("<input type='text' name='reponse' placeholder='Votre réponse...'/>")
            print("</div>")
            print("<button type='submit'>Envoyer</button>")
            print("</form>")
            affiche_reponse(r[0],cursor,id_sujet)
            print("</li>")
        print("</ul>")

print("<ul>")
for i in id_content_pseudo_parent :
    if i[3] == None :
        print("<li>")
        print(f"<p><b>{i[2]}</b> : {i[1]}</p>")
        print("<form action ='repondre.py' method='POST'>")
        print("<div>")
        print("<label>Répondre:</label>")
        print(f"<input type='hidden' name='id_parent' value='{i[0]}'/>")
        print(f"<input type='hidden' name='id_sujet' value='{id_sujet}'/>")
        print("<input type='text' name='reponse' placeholder='Votre réponse...'/>")
        print("</div>")
        print("<button type='submit'>Envoyer</button>")
        print("</form>")
        affiche_reponse(i[0],cursor,id_sujet)
        print("</li>")
    else:
        print()
print("</ul>")

print("<form action ='poster_message.py' method='POST'>")
print("<div>")
print("<label>Ajouter un commentaire:</label>")
print(f"<input type='hidden' name='id_sujet' value='{id_sujet}'/>")
print("<input type='text' name='contenu' placeholder='Votre message...'/>")
print("</div>")
print("<button type='submit'>Envoyer</button>")
print("</form>")
conn.close()
