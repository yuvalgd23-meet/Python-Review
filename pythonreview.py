def create_youtube_video(title, discription):
	
	dict1 = {"title": title, "discription": discription,"likes":0, "dislikes":0, "username":{} }
	return(dict1)

dict1=create_youtube_video("title", "discription")
print(dict1)
def likes (dict1):
	dict1["likes"] += 1
	return dict1

print(likes(dict1))


def dislikes (dict1):
	dict1["dislikes"] += 1
	return dict1

print(dislikes(dict1))

def comments(dict1):
	dict1["username"]= "noam is noob"
	return dict1
print(comments(dict1))
dict1 = create_youtube_video("noam", "npc")
for i in range (496):
	likes(dict1)
print(dict1)