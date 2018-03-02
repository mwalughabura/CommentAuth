import getpass

all_users={}

class User(object):
	usertype = "regular"

	def __init__(self,username,password):
		self.username = username
		self.password = password

	# def create_user(self):
	# 	pass
		

	def create_comment(self):
		pass

	def view_comments(self):
		pass

	def update_comment(self):
		pass

more_users = {}

print ("Hello weclcome to CommentAuth.")
if len (all_users) == 0:
	answer = input ("Do you have an account\n 1. Yes\n 2. No \n >>> ")

	if str(answer) == "No":
		username = input ("What is your username? \n >>> ")
		password = getpass.getpass ("Input a password please \n >>> ")
		all_users[username] = password
		new_user = User(username, password)
		all_users[username] = new_user
		print ("\nSuccessfully added new user\n")

	elif str(answer) == "Yes":
		pass

	else:
		print ("Invalid respose.")
		exit()


comment = input ("Write a comment about this app. \n >>> ")
more_users["first comment"] = comment

print ("Now edit the comment.\n\n")
comment = input ("Edit the comment that you wrote. \n >>> ")
more_users["second comment"] = comment

# print (all_users)

print ("\nThe first comment was '%s' now the comment is '%s'\n" %(more_users["first comment"], more_users["second comment"]))

# print ("Your username is: %s your password is :%s" %(username, password))
