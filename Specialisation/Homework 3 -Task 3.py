"""
A] Simulate clicking around the CFG Website. Keep track of the URL changes and
print the current URL after each move.
● You will need to display the options for each link, and include an option for
‘Back’ if not on the Base URL.
● You do not need to worry about error handling
● You are recommended to keep the simulation going within a while True loop
so the logic keeps looping until an exit is forced.
You only need to consider the following URLs for your solution:
1. Base URL: https://codefirstgirls.com/
2. Category URLs: /courses ,/opportunities/
3. Sub-category URLs: /courses/cfgdegree/ , /opportunities/ambassadors/
"""

import http.client

base_url = "https://codefirstgirls.com/"
current_url = ""


def sim_nav():
    global current_url

    # While true loop
    while True:
        # Base case
        print("Current URL:", current_url)

        # Connect to sever and get and read info
        connection = http.client.HTTPSConnection(base_url)
        connection.request("GET", current_url)
        response = connection.getresponse()
        html_content = response.read().decode('utf-8')
        # Links
        links = {
            1: "/courses",
            2: "/opportunities",
            3: "/courses/cfgdegree/",
            4: "/opportunities/ambassadors/"
        }

        # Iterate over the links
        for i, link in links.items():
            print(f"{i}. {link}")

        # Include an option for ‘Back’ if not on the Base URL
        if current_url != "":
            print("0. Back")

sim_nav()








