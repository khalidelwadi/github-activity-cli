import requests
import sys



user_args = sys.argv[1]
URL = f"https://api.github.com/users/{user_args}/events"

my_request = requests.get(URL)
data = my_request.json()

if len(data) <= 3 and data["status"] == '404':
    print("Username Not Found")
    exit(1)


output = []
live_output = []
count = 1
count_dict = {}
for i in data:
    if i["type"] == "PushEvent":
        text = f'Pushed {count} commits to {i["repo"]["name"]}'
        live_output.append(text)
    elif i["type"] == "CreateEvent":
        text = f'Created a {i["payload"]["ref_type"]} in {i["repo"]["name"]}'
        live_output.append(text)
    elif i["type"] == "PullRequestEvent":
        text = f'Created {count} pull request to {i["repo"]["name"]}'
        live_output.append(text)


for i in live_output:
    count_dict[i] = count_dict.get(i, 0) + 1

out_list  = ""
for i, j in count_dict.items():
    if j > 1:
        for k in i:
            if k == "1":
                out_list += f'{j}'
                continue
            out_list += k
        output.append(out_list)
        out_list = ""
        continue
    output.append(i)

for i in output:
    print(i)


