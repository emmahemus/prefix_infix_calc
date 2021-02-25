import requests


# function to handle prefix request
def prefix_request(prefix_input):
    url = "http://127.0.0.1:5000/prefix"

    payload = "{\"input\": " + prefix_input + "}"

    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


# function to handle infix request
def infix_request(infix_input):
    url = "http://127.0.0.1:5000/infix"

    payload = "{\"input\": " + infix_input + "}"

    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


prefix_input = "\"+ * 1 2 3\""
print(prefix_request("\" ( 56 ) \""))
