from maps import search

place = search.place_search_text("Pizza near Lille France", 1000, 0, 2, False, "restaurant")
print(place)