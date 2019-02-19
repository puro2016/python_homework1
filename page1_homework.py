# ___coding:utf-8___
# author:puro
# date:2019.02.18
#  use:page1_homework

'''User login program'''

# read user file as a dictionary
user_file = open('F:\python-study\page1\lock_user_file','r')
a = user_file.read()
user_info = eval(a)
user_file.close()

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
	-------your username or password not right,please try again-------
	-last %s times,if all wrong,the program exit and accout will lock-
	''' % times

	lock_info = '''
	----Sorry,your accout has locked,please contact the author-------
	'''

	if username not in user_info.keys():
		print(lg_fail_info)
		continue
	if user_info[username][1] == 'locked':
		print(lock_info)
		break
	elif user_info[username][0] == password:
		print(lg_sucs_info)
		break
	else:
		print(lg_fail_info)
else:
	if username in user_info.keys():
		user_info[username][1] = 'locked'
		user_file = open('F:\python-study\page1\lock_user_file','w')
		user_file.write(str(user_info))
		user_file.close()