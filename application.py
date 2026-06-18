import hashlib, hmac, json, requests, os
from dotenv import load_dotenv

load_dotenv()

howgood_application_secret = os.environ["HOW_GOOD_APPLICATION_SECRET"]

how_good_application_domain = os.environ["HOW_GOOD_APPLICATION_DOMAIN"]
how_good_application_endpoint = os.environ["HOW_GOOD_APPLICATION_ENDPOINT"]
application_submit_endpoint = how_good_application_domain + how_good_application_endpoint

email = os.environ["EMAIL"]
resume_url = os.environ["RESUME_URL"]
current_location = os.environ["LOCATION"]
linkedin_url = os.environm["LINKEDIN_URL"]
github_repo_url = os.environ["GITHUB_REPO_URL"]

payload = {
        "name": "Immanuel Currah",
        "email": email, 
        "resume": resume_url,
        "location": current_location,
        "linkedin": linkedin_url,
        "codeLink": github_repo_url,
        "yearsPython": 2,
        "yearsDjango": 0,
        }

json_formatted_payload = json.dumps(payload)

authentication_signature = hmac.new(secret.encode(), body.encode(), hashlib.sha256).hexidigest()

response = requests.post(
        application_submit_endpoint, 
        data=json_formatted_payload,
        heads={
            "Content-Type": "application/json",
            "X-HMAC-Signature": authentication_signature,
            },
        )
response_status_code = response.status_code
response_body = response.json()
print(response_status_code, response_body)
