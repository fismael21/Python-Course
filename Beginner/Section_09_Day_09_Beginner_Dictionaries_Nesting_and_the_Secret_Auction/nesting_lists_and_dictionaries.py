#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting a dictionary in a dictionary
travel_log_2 = {
  "France": { #Inner dictionary
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },

  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
  }
}

#Nesting a dictionary in a list
travel_log_2 = [
  #Dictionary 1
  { "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12,
  },

  #Dictionary 2
  { "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5,
  }
]