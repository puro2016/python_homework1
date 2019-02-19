# ___coding:utf-8___
# author:puro
# date:2019.02.18
#  use:page1_homework

'''User login program'''

# user info dictionary
user_info = {
	'puro':'1234321',
	'arens':'654789',
	'far':'3333'
	}

# open file of locked user
lock_file = open('F:\python-study\page1\lock_user_file','r')

# user try login times
times = 3

# user login
while times > 0:
	times -= 1
	username = input("please input your name:")
	password = input("please input your password:")

	lg_sucs_info = '''
	---------------welcome %s---------------
	''' % username

	lg_fail_info = '''
	----your username or password not right,please try again---------
	----you also can try %s times,if all wrong,you accout will lock--
	''' % times

	lock_info = '''
	----Sorry,your accout has locked,please contact the author-------
	'''

	if username in lock_file.readlines():
		print(lock_info)
		break
	elif (username in user_info
			and password == user_info[username]):
		print(lg_sucs_info)
		break
	else:
		print(lg_fail_info)
else:
	print(lock_info)
	lock_file.close()
	lock_file = open('F:\python-study\page1\lock_user_file','a')
	lock_file.write(username+'\n')

lock_file.close()