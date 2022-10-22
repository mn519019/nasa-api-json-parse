# nasa-api-json-parse
Json file parsing using NASA's APIs

- A python script to parse JSON data using one of the NASA's APIs. It uses Neo - Feed Open Api to get data using start_date and end_date. 
- We can search expected incoming asteroid by searching a specific period. 
- Example Query : https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY

# Requirement
- python 3 

# Approach 
- When you GET data by sending a HTTP request on python, the data can be cut off on your terminal. I normaly use this site if the api link is provided [JSON Formatter](https://pages.github.com/](https://jsonformatter.org/json-pretty-print).

#### Reference: 
- https://api.nasa.gov/
