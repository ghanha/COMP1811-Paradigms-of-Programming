#Student ID: 001052068
#Hackathon: Task 1.5.

import sqlite3
def hackathon_task5():
    counts = {}
    c = sqlite3.connect("login.db")

    """
    ids = c.execute("SELECT CANDIDATE FROM COUNTING WHERE POSITION='President' AND PREFERENCE = (SELECT MAX(PREFERENCE) FROM COUNTING WHERE PREFERENCE IN(SELECT DISTINCT TOP 4 PREFERENCE FROM COUNTING ORDER BY PREFERENCE DESC").fetchall()
    #Compared to our group initial database "login.db",
    # New DB has been updated with more candidates for "President" position
    #Following a list mention in Hackathon Task 1.4.
    print(ids)
    """

    ids = c.execute("SELECT NAME FROM Candidates WHERE POSITION='President'").fetchall()
    for x in ids:
        name = (x[0])
        votes = c.execute("SELECT PREFERENCE FROM COUNTING WHERE CANDIDATE = ? ORDER BY PREFERENCE DESC",(name,)).fetchone()[0]
        counts[name] = votes
    #Single Transferable vote
    print("Top 3 candidates are: ", counts)

hackathon_task5()