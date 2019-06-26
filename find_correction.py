
import os, sys, requests
import time
import simplejson as json
import argparse
import pickle
from progress.bar import ChargingBar
from tabulate import tabulate

def connection_api():
	args = [
		'grant_type=client_credentials',
		'client_id=' + os.environ["FT42_UID"],
		'client_secret=' + os.environ["FT42_SECRET"],
	]
	status = requests.post("https://api.intra.42.fr/oauth/token?%s" % ("&".join(args)))
	token = status.json()
	
	if not status.status_code == 200:
		print("You are not connecting to the 42 API please check README.md")
		sys.exit()
	return status.json()

def clear():
	sys.stdout.write("\033[F")
	sys.stdout.write("\033[K")

def get_id_project(name_project, token):
	print("Get id of the project")
	clear()
	args = [
	'access_token=%s' % (token['access_token']),
	'token_type=bearer',
	'filter[name]=' + str(name_project),
		]
	status = requests.get("https://api.intra.42.fr/v2/projects?%s" % ("&".join(args)))
	if not status.status_code == 200:
		print("Error during project search.")
		sys.exit()
	response = status.json()
	try:
		return response[0]['id']
	except:
		print("Project {} not find. Please check your spelling.".format(name_project))
		sys.exit()

def get_user_who_make_the_project(id, token, argument):
	page = 0
	all_user = get_buffer_file(argument)
	if not all_user or argument.update:
		print("Get all users who register the project {} (Can take some time the first time...)".format(argument.name_project))
		bar = None
		while (1):
			args = [
			'access_token=%s' % (token['access_token']),
			'token_type=bearer',
			'page[size]=100',
			'page[number]={}'.format(str(page)),
				]
			status = requests.get("https://api.intra.42.fr/v2/projects/" + str(id) + "/projects_users?%s" % ("&".join(args)))
			if not status.status_code == 200:
				print("Error during projects users search.")
				sys.exit()
			if not bar:
				bar = ChargingBar('Call API 42', max=(int(status.headers['X-Total']) // 100) + 2)
			response = status.json()
			if not response:
				break
			for projet in response:
				for team in projet['teams']:
					for user in team['users']:
						all_user[user['login']] = [projet['status'], projet['validated?'], projet['final_mark']]
			page += 1
			bar.next()
			time.sleep(1)
		bar.finish()
		clear()
		clear()
		create_buffer_file(argument, all_user)
	return all_user

def create_buffer_file(args, people_we_want):
	try:
		with open(".{}.txt".format(args.name_project.replace(" ", "_")), "wb") as fp:   #Pickling
			pickle.dump(people_we_want, fp)
	except:
		print("Error")
		exit(0)

def get_buffer_file(args):
	b = {}
	try :
		with open(".{}.txt".format(args.name_project.replace(" ", "_")), "rb") as fp:   # Unpickling
			b = pickle.load(fp)
	except:
		pass
	return b


def get_id_campus(arguments):
	print("Get id of the campus")
	clear()
	args = [
	'access_token=%s' % (token['access_token']),
	'token_type=bearer',
	'filter[name]=' + str(arguments.campus),
		]
	status = requests.get("https://api.intra.42.fr/v2/campus?%s" % ("&".join(args)))
	if not status.status_code == 200:
		print("Error during campus search.")
		sys.exit()
	response = status.json()
	time.sleep(1)
	try:
		return response[0]['id']
	except:
		print("Campus {} not find. Please check your spelling.".format(arguments.campus))
		sys.exit()


def get_all_people_connected(token, args):
	all_user = []
	page = 0
	if args.campus == "Paris":
		id_campus = 1
	else:
		id_campus = get_id_campus(args)
	print("Get all peaple who is actually connected in {}".format(args.campus))
	clear()
	bar = None
	while (1):
		args = [
		'access_token=%s' % (token['access_token']),
		'token_type=bearer',
		'page[size]=100',
		'page[number]={}'.format(str(page)),
		'filter[active]=true',
			]
		status = requests.get("https://api.intra.42.fr/v2/campus/" + str(id_campus) + "/locations?%s" % ("&".join(args)))
		if not status.status_code == 200:
			print("Error during people connected search.")
			sys.exit()
		if not bar:
			bar = ChargingBar('Call API 42', max=(int(status.headers['X-Total']) // 100) + 2)
		response = status.json()
		if not response:
			break
		for poste in response:
			all_user.append([poste['user']['login'], poste['host']])
		page += 1
		bar.next()
		time.sleep(1)
	bar.finish()
	clear()
	return all_user

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("name_project", help="Name of the project your search for correction", type=str)
	parser.add_argument("--campus", help="Name of your Campus. Default is Paris", type=str, default="Paris")
	parser.add_argument("--update", help="Update user who validate the current project.", action="store_true")
	args = parser.parse_args()

	if not os.environ["FT42_UID"] or not os.environ["FT42_SECRET"]:
		print("You need to export environnement variable FT42_UID and FT42_SECRET. See README.md .")
		sys.exit()

	token = connection_api()
	id_project = get_id_project(args.name_project, token)
	
	people_we_want = get_user_who_make_the_project(id_project, token, args)
	
	people_here = get_all_people_connected(token, args)

	possible_corrector = []

	for here in people_here:
		if here[0] in people_we_want:
			possible_corrector.append([here[0], str(people_we_want[here[0]][0]), str(people_we_want[here[0]][1]), str(people_we_want[here[0]][2]), here[1]])
	
	possible_corrector_no_duplicate_value = [] # Remove duplicate value
	for corrector in possible_corrector:
		if not corrector[0] in [x[0] for x in possible_corrector_no_duplicate_value]:
			possible_corrector_no_duplicate_value.append(corrector)
	possible_corrector = possible_corrector_no_duplicate_value

	if not possible_corrector:
		print("No corrector found for this project")
	else:
		print(tabulate(possible_corrector, headers=['Login', 'Project status', 'Validated', 'Final Mark', 'Position']))
