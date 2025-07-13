capitals = {
    "France0": "Paris",
    "Germany": "Berlin"
}

#nesting a list in a dectionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#nesting a dictionary in dictionary
travel_log = {
    "France": {
                "cities_visited": ["Paris", "Lille", "Dijon"], 
                "total_visits": 12
                },
    "Germany": {
                "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
                "total_visits": 5
                }
}

#nesting a list in dictionary
travel_log = [
    {
        "Country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "Country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
    }
]