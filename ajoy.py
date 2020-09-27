  
print("content-type: text/html")
print()
import subprocess as sp
import cgi
form=cgi.FieldStorage()
cmd=form.getvalue("x")

if(cmd=="Open Notepad"):
	sp.getoutput("notepad")
elif(cmd=="Open Chrome"):
	sp.getoutput("chrome")
elif(cmd=="Open Firefox"):
	sp.getoutput("firefox")
elif(cmd=="virtualbox"):
	sp.getoutput("virtualbox")
elif(cmd=="Show Calendar"):
	sp.getoutput("cal")
elif(cmd=="Show Today's Date")
	sp.getoutput("Date")
else:
	print("You entered wrong input\n")
