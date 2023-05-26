def traveltime (distance, speed): #distancce,don't forget the final answer will be in MINUTES
    return distance / speed * 60 # distance (km) / speed (km/h) to find hours, then multiply by 60 to get minutes

t = traveltime(45, 200) # V = d/t
print(t)
