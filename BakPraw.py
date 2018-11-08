import praw
import urllib.request
from PIL import Image
import ctypes

reddit = praw.Reddit(client_id = "zJHOdeFAHlnQqQ", client_secret = "mgayqqHtoZ0THc_y1onYDxJUkf4", username="potetsos", password="BakgrunnPassord", user_agent="test")





#subreddit.subscribe()

def finnLink():



	subreddit = reddit.subreddit("EarthPorn")

	hotPost = subreddit.top("day")
	#hotPost = subreddit.hot()


	#optimalt = 16/9
	#print(optimalt)

	nummerPost = 0

	for post in hotPost:



		nummerPost += 1

		#print(post.url)
		#print(post.title)
		teller = 0
		var = False

		tall2 = ""
		tall1 = ""	

		string = post.title
		for i in range (len(string)):
			
			bokstav = string[len(string)-i -1]
			#print(bokstav)



			if (bokstav.isdigit()):
				if (var == False):
					teller+=1
				var = True
				if (teller ==1):
					tall2 += (bokstav)
				if (teller == 2):
					tall1 += (bokstav)

			else:
				var = False
				if (teller == 2):
					break


			#print(bokstav)
			#print(bokstav.isdigit())

		tall1 = tall1[::-1]
		tall2 = tall2[::-1]

		#print(tall1)
		#print(tall2)

		tall1 = int(tall1)
		tall2 = int(tall2)

		try:
			
			if (1.27 < tall1/tall2 < 2.7):
				#print(tall1/tall2)
				print("Titell      : " + post.title)
				print("Oppløysing  : " + str(tall1) + " X " + str(tall2))
				match = (tall1/tall2) / (16/9)
				print("Størelse    : " + str(match * 100) + "%")

				print("Post Nummer : " + str(nummerPost))

				print("Score       : " + str(post.score))



				#print(post.url)

				return(post.url)



				break

		except:
			print("feil")

		#break

	return("fant ingen ting")

#finnLink()


def main():
	link = finnLink()
	#print(link)
	print("\n")
	print("Laster ned bilde frå reddit")

	urllib.request.urlretrieve(link, "C:/Users/Toft/Pictures/reddit/bilde.jpg")

	
	ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/Toft/Pictures/reddit/bilde.jpg" , 1)



main()