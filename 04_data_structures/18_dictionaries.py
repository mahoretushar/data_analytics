# key, value pair
# points = {"x": 1, "y": 2}
# points["x"]
# points["y"]


# points = [1, 2]
# points[0]
# points[1]


# SQL     and     NoSQL
# tables  and     documents = {key: value}


points = {"x": 1, "y": 2}
# points = dict(x=1, y=2)
points["z"] = 100
print(points)

if "p" in points:
    print(points["p"])


print(points.get("p", "Not Exists"))


# del points
# print(points)


for x in points:
    print(x, points[x])


for x in points.items():
    print(x)


for key, val in points.items():
    print(f"{key}-------{val}")
