car_velocity= int(input( "enter V km/h:"))

if car_velocity < 0:
    print("impossible velocity")
elif car_velocity < 30:
    print("very slow")
elif car_velocity < 60:
    print("moderate")
elif car_velocity < 120:
    print("fast")
else:
    print("very fast")
