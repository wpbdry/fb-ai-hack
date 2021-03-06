import requests

# URL which return JSON string
url = 'https://www.eventbriteapi.com/v3/events/?token=YQVEX6PF66QPHON2KHD3'

# Get list of events
request_string = requests.get(url)
request_array = request_string.json()
events = request_array['events']

# Add event descriptions to txt files
for item in events:
    description = item['description']['text']
    if description:
        # Replace \n, \r, weird space, -, and leading and trailing spaces
        description = description.replace('\n', ' ')
        description = description.replace('\r', ' ')
        description = description.replace(' ', ' ')  # weird character that exists in descriptions that is not a space
        description = description.replace('-', ' ')
        description = description.strip()

        # Get rid of double spaces generated by all the replacing
        old_string = ''
        while description != old_string:
            old_string = description
            description = description.replace('  ', ' ')

        # Check for category file, if doesnt exist, create new file
        filename = 'categories/' + str(item['category_id']) + '.txt'
        file = open(filename, 'a')

        # Add description to file, separate descriptions with \n
        file.write(description)
        file.write('\n')
        file.close()
