# # Problem 1: Building a Playlist
# class SongNode:
# 	def __init__(self, song, next=None):
# 		self.song = song
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print(current.song, end=" -> " if current.next else "")
#         current = current.next
#     print()
		
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

# print_linked_list(top_hits_2010s)

# # Problem 2: Top Artists
# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
# 		self.artist = artist
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# def get_artist_frequency(playlist):
# 	freq = {}
# 	current = playlist
# 	while current: # Traverse the linked list
# 		freq[current.artist] = freq.get(current.artist, 0) + 1
# 		current = current.next
# 	# Return the frequency dictionary
# 	return freq

# playlist = SongNode("Saturn", "SZA", 
#                 SongNode("Who", "Jimin", 
#                         SongNode("Espresso", "Sabrina Carpenter", 
#                                 SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

# # Problem 3: Glitching Out
# class SongNode:
#     def __init__(self, song, artist, next=None):
#         self.song = song
#         self.artist = artist
#         self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()


# # Function with a bug!
# def remove_song(playlist_head, song):
#     if not playlist_head:
#         return None
#     if playlist_head.song == song:
#         return playlist_head.next

#     current = playlist_head
#     while current.next:
#         if current.next.song == song:
#             current.next = current.next.next  
#             return playlist_head 
#         current = current.next

#     return playlist_head


# playlist = SongNode("SOS", "ABBA", 
#                 SongNode("Simple Twist of Fate", "Bob Dylan",
#                     SongNode("Dreams", "Fleetwood Mac",
#                         SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))

# # Problem 4: On Repeat
# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
# 		self.artist = artist
# 		self.next = next

# # 1 solution - set()
# def on_repeat(playlist_head):
# 	passed = set()
# 	current = playlist_head
# 	while current:
# 		if current.song in passed:
# 			return True
# 		passed.add(current.song)
# 		current = current.next
# 	return False

# # 2 solution - fast and slow pointer
# def on_repeat(playlist_head):
#      """
#      Fast and slow pointer
#      if fast reaches end, return false
#      if fast == true return True
#      """
#      fast = playlist_head
#      slow = playlist_head
#      while fast and fast.next:
#          slow = slow.next
#          fast = fast.next.next

#          if fast == slow:
#              return True
#      return False

# song1 = SongNode("GO!", "Common")
# song2 = SongNode("N95", "Kendrick Lamar")
# song3 = SongNode("WIN", "Jay Rock")
# song4 = SongNode("ATM", "J. Cole")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(on_repeat(song1))

# # Problem 5: Looped
# class SongNode:
# 	def __init__(self, song, artist, next=None):
# 		self.song = song
# 		self.artist = artist
# 		self.next = next

# # For testing
# def print_linked_list(node):
#     current = node
#     while current:
#         print((current.song, current.artist), end=" -> " if current.next else "")
#         current = current.next
#     print()

# def loop_length(playlist_head):
#     fast = playlist_head
#     slow = playlist_head

#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#         if fast == slow: # there is a cycle
#             fast = fast.next
#             count = 1
#             while fast != slow:
#                 fast = fast.next
#                 count += 1
#             return count
#     return 0


# song1 = SongNode("Wein", "AL SHAMI")
# song2 = SongNode("Si Ai", "Tayna")
# song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
# song4 = SongNode("La", "DYSTINCT")
# song1.next = song2
# song2.next = song3
# song3.next = song4
# song4.next = song2

# print(loop_length(song1))

# Problem 6: Volume Control
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def count_critical_points(song_audio):
	pass

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))