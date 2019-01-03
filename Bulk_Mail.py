import smtplib #Simple mail transfer protocol.......
import getpass #Password hiding module..............
def get_userid():
	sender = input("Please enter your email:\n")
	return sender
def get_userpassword():
	sender_password = getpass.getpass("Please enter your password:\n")
	return sender_password
def take_id(teacher_message,subject,sender,sender_password):
    d={}#Declare a dictionary to map Student Name and Parent Email
    n=int(input("Please enter the number of recepients:\n"))#Integer taking number of recepients as input..
    for i in range(n):
        print("Enter the name of student " +str(i+1)+":")
        student_name=input()
        print("Enter the valid email id of parent: ")
        parent_id=input()
        d[student_name]=parent_id
        #Dictionary has name as key and parent's email id as value..
        #message_with_name=teacher_message.replace("$SNAME$",i)#RETURNS THE ENTERED MESSAGE WITH STUDENT NAME..
        #parent_id=d[i]#Parent ID is the value stored in the dictionary with name as key...
    send_mail(teacher_message,subject,sender,sender_password,d)

def input_message():#TAKE MESSAGE FROM TEACHER ONLY ONE TIME..
	msg=""
	temp=""
	print("Please Enter the Message to be sent,Enter the string $SNAME$ where ever you want the student name to be displayed,Enter the word END on a newline to stop your Message:")
	while temp!="END\n":
		temp=input()
		temp+='\n'
		msg+=temp
	return(msg[:len(msg)-4])#Returns Message from the Teacher as a string, after removing END
def input_subject():
    subject=input("Enter the Subject of the Message:")
    return subject

def send_mail(message,subject,sender,sender_password,d):
    k=1 #Count
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.gmail.com','465')
        print("Connecting to Mail Server")
        smtpObj.ehlo()#hello. ..
        print("Sending Hello Packets")
        #smtpObj.starttls()# securing using tls
        #print("Starting TLS...")
        smtpObj.login(sender,sender_password)#Login using the sender's Id and Password..
        print("Logged in")
        for receiver in d:
        	message_with_name=message.replace("$SNAME$",receiver)
        	smtpObj.sendmail(sender,d[receiver],'Subject:'+subject+'\n'+message_with_name+'\n')
        	print("Email " +str(k)+ " sent.")
        	k+=1 #Increment count..
        smtpObj.quit()
        print("Done.")
    except smtplib.SMTPHeloError:
    	print("Server did not reply to 'HELO' greeting.")
    except smtplib.SMTPServerDisconnected:
    	print("Server Disconnected.")
    except smtplib.SMTPSenderRefused:
    	print("Sender Refused")
    except smtplib.SMTPAuthenticationError as e:
    	print("Authentication Error Occured:\n"+str(e))
    except e:
    	print("Sorry something went wrong, check your internet connection.")
    	print("Message:"+str(e))

#GET THE TEACHER's MESSAGE....
if __name__=="__main__":
	id=get_userid()
	password=get_userpassword()
	subject=input_subject()#Holds the Subject..
	teacher_message=input_message()#Takes Teacher's Message..
	take_id(teacher_message,subject,id,password)
	#input()


