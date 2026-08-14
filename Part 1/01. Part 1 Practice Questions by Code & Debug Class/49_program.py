# Create a list of 5 of your favorate movies . print the first, lat and middle from your list using both positive and negative indexing where appropriate

movies = ["Bahubali", "Ved", "Tanhaji", "Sairat", "3 Idiots"]
print(movies[0])
print(movies[-len(movies)])
print(movies[-1])
print(movies[len(movies)-1])
print(movies[2])
print(movies[int((len(movies)-1)/2)]) # floor division also used
