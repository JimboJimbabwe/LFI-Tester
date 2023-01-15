import requests



# Read the list of paths from the file
with open('paths.txt', 'r') as f:
    paths = f.readlines()

# Iterate through the list of URLs
for url in urls:
    # Strip leading/trailing whitespace from the URL
    url = input("enter the URL you want to check for LFI: ")
    for path in paths:
        path = path.strip()
        new_url = url + path
        # Send an HTTP GET request to each new URL
        response = requests.get(new_url)

        # Check if the status code is 200
        if response.status_code == 200:
            print(f'{new_url} returned status code 200')
        else:
            print(f'{new_url} returned status code {response.status_code}')

