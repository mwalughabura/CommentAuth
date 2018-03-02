import getpass

all_users=[]

class User(object):
	usertype = "regular"

	def __init__(self,username,password):
		self.username = username
		self.password = password

	def create_user(self):
		pass
		

	def create_comment(self):
		pass

	def view_comments(self):
		pass

	def update_comment(self):
		pass

print ("Hello weclcome to CommentAuth.")
if len (all_users) == 0:
	answer = input ("Do you have an account\n 1. Yes\n 2. No \n >>> ")
	# while  answer != "Yes" or answer != "No":
	# 	username = input ("Input either Yes or No :: The first letter is capital. \n >>> ")
	if answer == "No":
		username = input ("What is your username? \n >>> ")
		password = getpass.getpass ("Input a password please \n >>> ")
	elif answer == "Yes":
		pass
		
	print ("%s %s" %(username, password))