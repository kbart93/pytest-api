import requests
import json

def test_get_user():
    p = {"page": 2}
    resp = requests.get("https://reqres.in/api/users", params=p)
    json_response = resp.json()

    print(json_response["total_pages"])
    assert json_response["total_pages"] == 2, "total pages doesn't match"
    print(json_response["total"])
    assert json_response["total"] == 12, "total doesn't match"
    print(json_response["data"][0]["email"])
    assert json_response["data"][0]["email"], "invalid email"
    print(json_response["support"]["url"])
    assert (json_response["support"]["url"].endswith("heading")), "url wrong"
    print(json_response["data"][0]["last_name"])
    assert json_response["data"][0]["last_name"] != None

def test_get_statuscode():
    url = "https://reqres.in/api/users"
    resp = requests.get(url)
    code = resp.status_code
    assert code == 200, "Code doesn't match"

def test_create_user():
    payload = {
        "name": "Jan",
        "job": "Automation"
    }

    resp = requests.post("https://reqres.in/api/users", data=payload)
    print(resp.json())
    assert resp.json()["job"] == "Automation", "wrong data!"
    assert resp.json()["name"] == "Jan", "wrong data!"

    data2 = {
        "name": "Kuba",
        "job": "Soldier"
    }

    response = requests.post("https://reqres.in/api/users", data=data2)
    print(response.json())
    assert response.json()["job"] == "Soldier", "wrong data!"
    assert response.json()["name"] == "Kuba", "wrong data!"

def test_create_user_from_file():
    mydata = open("data.json", "r").read()
    resp = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
    print(resp.json())
    assert resp.json()["job"] == "Policeman", "wrong data!"
    assert resp.json()["name"] == "Tom", "wrong data!"

def test_put_patch():

    #PUT

    mydata = {
        "name": "Tim",
        "job": "Doctor"
    }

    resp = requests.put("https://reqres.in/api/users/2", data=mydata)

    assert resp.status_code == 200
    assert resp.json()["job"] == "Doctor"
    print(resp.json())

    # PATH

    mydata2 = {
        "name": "Tim"
    }
    response = requests.patch("https://reqres.in/api/users/2", data=mydata2)
    assert response.json()["name"] == "Tim"
    print(response.json())

def test_delete_user():
    resp = requests.delete("https://reqres.in/api/users/2")
    print(resp.status_code)
    assert resp.status_code == 204, "User deletion failed"