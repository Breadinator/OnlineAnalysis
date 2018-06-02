import json #not used in the actual program, but I used it for testing and I'm lazy af
from urllib.request import urlopen
from time import sleep #1 api call a second max

class get: #all get.*() function args given as strings or ints where appropriate
	def boards():
		url = "https://a.4cdn.org/boards.json"
		return urlopen(url).read().decode()

	def catalog(board):
		url = "https://a.4cdn.org/" + str(board) + "/catalog.json"
		return urlopen(url).read().decode()

	def archive(board):
		url = "https://a.4cdn.org/" + str(board) + "/archive.json"
		return urlopen(url).read().decode()

	def threads(board):
		url = "https://a.4cdn.org/" + str(board) + "/threads.json"
		return urlopen(url).read().decode()

	def thread(board, thread):
		url = "https://a.4cdn.org/" + str(board) + "/thread/" + str(thread) + ".json"
		return urlopen(url).read().decode()

	def reply(board, thread, reply):
		url = "https://a.4cdn.org/" + str(board) + "/thread/" + str(thread) + "#p" + str(reply) + ".json"
		return urlopen(url).read().decode()

class mass: #arg "boards" given as tuple or array
	def catalog(boards):
		catalogs = {}
		for i in boards:
			catalogs[i] = get.catalog(i)
			sleep(1)
		return catalogs

	def archive(boards):
		archives = {}
		for i in boards:
			archives[i] = get.archive(i)
			sleep(1)
		return archives

	def threads(boards):
		threads = {}
		for i in boards:
			threads[i] = get.threads(i)
			sleep(1)
		return threads