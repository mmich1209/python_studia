# jesli temperatura dodatnia i sun shining to pojdziemy na spacer
temp = 12
is_sun_shining = False

if temp > 0 and is_sun_shining:
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-" * 50)

# jezeli bedzie ujemna temperatura lub bedzie pochmurnie
# to zostaniemy w domu a jezeli nie to idziemy na spacer

if not (temp < 0 or not is_sun_shining):
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")


