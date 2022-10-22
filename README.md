## nasa-api-json-parse
Json file parsing using NASA's APIs

- A python script to parse JSON data using one of the NASA's APIs. It uses Neo - Feed Open Api to get data using start_date and end_date. 
- We can search expected incoming asteroid by searching a specific period. 
- Example Query : https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

## Requirement
- python 3 
- Your own api key from NASA's website
- Understanding the queried JSON structure Main Json Obj vs Array of objects (dictionary)

## Approach 
- When you GET data by sending a HTTP request (request moduel) from python, the data can be cut off on your terminal. I normaly use this site if the api link is provided [JSON Formatter](https://jsonformatter.org/json-pretty-print).
- Otherwise, store your targeted data in the textbox when JSON file is very lengthy

## Reference: 
- https://api.nasa.gov/
