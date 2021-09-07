# Sending-emails-using-python-and-excel

Sometimes, we need to send emails to multiple users, cold emails etc. and doing that manually is a time-consuming and error-prone task, but it’s easy to automate with Python <br/>

Simple Mail Transfer Protocol (SMTP) is a protocol, which handles sending e-mail and routing e-mail between mail servers.<br/>
Python comes with the built-in smtplib module for sending emails using the SMTP.
Syntax: </br>
import smtplib<br/>

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] ) </br>

