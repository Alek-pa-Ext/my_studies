from pprint import pprint
biggest_cities = ["Tokyo", "Delhi", "Shanghai", "Mexico City", "Sao Paulo",
                  "Mumbai", "Kinki major metropolitan area", "Cairo"]

pairs = zip(biggest_cities, range(1, 9))
pprint(list(pairs))