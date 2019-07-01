#!/usr/bin/python3                                                                                                                                                      
                                                                                                                                                                        
import mysql.connector as mysql                                                                                                                                         
#RDS info                                                                                                                                                               
u='root'                                                                                                                                                                
p='*******'                                                                                                                                                          
db='adhoc'                                                                                                                                                              
h='mydbserver.cbavvvkuwa8t.ap-south-1.rds.amazonaws.com'                                                                                                                
                                                                                                                                                                        
                                                                                                                                                                        
#now connecting                                                                                                                                                         
conn=mysql.connect(user=u,password=p,database=db,host=h)                                                                                                                
# now generating a sql lang cursor                                                                                                                                      
cur=conn.cursor()                                                                                                                                                       
                                                                                                                                                                        
#now we can write sql query                                                                                                                                             
                                                                                                                                                                        
cur.execute("show tables;")                                                                                                                                             
#now print result                                                                                                                                                       
print(cur.fetchall())                                                                                                                                                   
#closing conn                                                                                                                                                           
conn.close()  
