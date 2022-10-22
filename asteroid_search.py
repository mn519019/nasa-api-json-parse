# Import request lib
import requests

# Quick note
# Making subsequent api requests may return OVER_RATE_LIMIT
# Therefore, working on the copied json data would be a good start, you can also create your own API KEY
# Example Query: https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

###### Variables ######
start="2015-09-06"
end="2015-09-07"
url = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+str(start)+"&end_date="+str(end)+"&api_key=<Generated API Key"
######################

def json_parse(arg1):
    response = requests.get(arg1)
    response_json = response.json()
    dates = response_json["near_earth_objects"]
    status = response.status_code

# Check status code 
    if status == 200:
        asteroid_counter = 0
        for date in dates:
            for astroid in dates[date]:
                    if astroid["is_potentially_hazardous_asteroid"] == True:
                        asteroid_counter +=1
        return "Total number of potentially hazardous asteroids from period " + start + " to " + end + "is "+ str(asteroid_counter)
                    
    else:
        print("HTTP Status code 200 is not returned, and got ",status)



## Possible smtp implementation to get notified.
## TBC ...



# Calling a function
print(json_parse(url))

## Expected output
#Total number of potentially hazardous asteroids from period 2015-09-06 to 2015-09-07 is 1



