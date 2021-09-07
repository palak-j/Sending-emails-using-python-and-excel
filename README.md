# Sending-emails-using-python-and-excel

Sometimes, we need to send emails to multiple users, cold emails etc. and doing that manually is a time-consuming and error-prone task, but it’s easy to automate with Python <br/>

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.<br/>
Python comes with the built-in smtplib module for sending emails using the SMTP.
Syntax: </br>
import smtplib<br/>

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] ) </br>
host − This is the host running your SMTP server(optional). </br>
port − If you are providing host argument, then you need to specify a port, where SMTP server is listening. </br>
local_hostname − If your SMTP server is running on your local machine, then you can specify just localhost. </br></br>

An SMTP object has an instance method called sendmail, which is used to mailing a message. It takes three parameters − </br> Sender </br> Receiver </br> Message </br>





#### Python documentation : 
#### https://docs.python.org/3/library/smtplib.html


