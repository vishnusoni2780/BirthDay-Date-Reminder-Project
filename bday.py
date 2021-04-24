import sqlite3
import pyttsx3 as pys

conn=sqlite3.connect("bday.sqlite")

cur=conn.cursor()

cur.execute("DROP TABLE DATA;")
cur.execute("""CREATE TABLE DATA(
	Name TEXT NOT NULL,
	BDate VARCHAR NOT NULL
	);
	""")

print("="*53)
print(">>>\tWelcome to Birthday Reminder App\t<<<")
print("="*53)

print(">>>\tWhat can i do for you?\n")
#pys.speak("What can i do for you.")
print("""\t\t1. Make a New Record.
		2. Fetch a Record.
		3. Update a Record.
		4. Delete something.""")
print("="*53)
pys.speak("please enter number of your choice")
while True:
	choice=int(input("\nEnter your Chioce: "))

	if choice==1:
		N=input("Enter the Name: ")
		BD=input("Enter the Birthday Date(DD/MM/YY): ")
		cur.execute("INSERT INTO DATA (Name,BDate) VALUES (?,?)",(N,BD))
		cur.execute("commit;")
		r=cur.execute("select * from DATA")
		print(r)

	if choice==2:
		val=input("Enter Name of your friend to fatch his/her B'Day Date: ")
		r=cur.execute("SELECT BDate FROM DATA WHERE NAME=?;",val)
		print(r)

	if choice==3:
		NOF=input("Enter name of friend whose B'Day Date to be update: ")
		NBD=input("Enter New Birthday Date: ")
		cur.execute("UPDATE DATA set BDate=? WHERE Name=?;",(NBD,NOF))
		cur.execute("commit;")
		
	if choice==4:
		pys.speak("which friend's record you want to Delete.")
		DOR=input("Enter Name of that Friend: ")
		cur.execute("DELETE FROM DATA WHERE NAME=?;",DOR)
		cur.execute("commit;")

	if choice==00:
		break

	if choice!=1 and choice!=2 and choice!=3 and choice!=4 and choice!=00:
		pys.speak("Um Hm, Invalid choice.")
		print("Please enter a Valid Choice.")