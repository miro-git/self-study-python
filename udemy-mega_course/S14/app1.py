import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

w = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % w)
results = cursor.fetchall()

if results:
    for r in results:
        print(r[1])
else:
    print("The word '%s' does not exist in our dictionary." % w)



