import requests
import json

# Replace these with your GitHub repository information and personal access token
owner = "Fiserv"
repo = "Testing-repo"
#token = "YOUR_PERSONAL_ACCESS_TOKEN"

# Function to get a list of hook IDs for the repository
def get_hook_ids():
    url = f"https://api.github.com/repos/{owner}/{repo}/hooks"
    headers = {
        "Authorization": f"Bearer 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",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    hooks = response.json()
    hook_ids = [hook["id"] for hook in hooks]
    return hook_ids

# Function to redeliver failed deliveries with status code 500
# def redeliver_failed_deliveries(hook_id):
#     url = f"https://api.github.com/repos/{owner}/{repo}/hooks/{hook_id}/deliveries"
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Accept": "application/vnd.github.v3+json"
#     }

#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
#     deliveries = response.json()

#     for delivery in deliveries:
#         if delivery["response"]["status"] == 500:
#             delivery_id = delivery["id"]
#             redeliver_url = f"https://api.github.com/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts"
#             response = requests.post(redeliver_url, headers=headers)
#             response.raise_for_status()
#             print(f"Redelivered delivery ID {delivery_id} for hook ID {hook_id}")

if __name__ == "__main__":
    hook_ids = get_hook_ids()
    # for hook_id in hook_ids:
    #     redeliver_failed_deliveries(hook_id)
