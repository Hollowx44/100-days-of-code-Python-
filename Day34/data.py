import requests
parameter={
    "amount":10,
    "type":"boolean",
    "category":31
}
q_data=requests.get(url="https://opentdb.com/api.php",params=parameter)
q_data.raise_for_status()
question_data=q_data.json()["results"]