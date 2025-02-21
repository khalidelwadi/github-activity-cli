# github-activity-cli


Provide the GitHub username as an argument when running the CLI.

python3 github-activity <username>

Fetch the recent activity of the specified GitHub user using the GitHub API. You can use the following endpoint to fetch the user’s activity:

https://api.github.com/users/<username>/events

Display the fetched activity in the terminal.
Output:
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- ...


inspired from :
https://roadmap.sh/projects/github-user-activity