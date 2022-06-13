import json

with open("contrasenas.txt") as file:
    # Read each website in the file
    websites = file.readlines()
    # Format each website into a [site, email, password] list
    websites_formatted = [website.strip().split(",") for website in websites]
    # Convert each list into a dictionary
    websites_dict = {website_data[0]: {"email": website_data[1], "password": website_data[2]}
                     for website_data in websites_formatted}

with open("data.json", "w") as file:
    json.dump(websites_dict, file, indent=4)
