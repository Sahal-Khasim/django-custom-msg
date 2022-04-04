import threading
from time import sleep
import requests





class CreateStudentsThread(threading.Thread):

    def __init__(self, message, number, btn_mobile, btn_mobile_name, url_btn, url_btn_name):

        self.message = message
        self.number = number
        self.btn_mobile = btn_mobile
        self.btn_mobile_name = btn_mobile_name
        self.url_btn = url_btn
        self.url_btn_name = url_btn_name
        threading.Thread.__init__(self)

    def run(self):
        try:
            print("thread started")
            for i in range(len(self.number)):
                print(i)
                print(self.number[i])
                if(len(self.message)):
                    API_URL = "http://api.wall.town/api/send-text"

                    data = {
                        "number" : self.number[i],
                        "msg" : self.message,

                        "instance" : "68e41486aaa1fc1e8a87f579f769eb6d274816bdce1577c4dbfcda1f18ff5cca",
                        "apikey" : "89579afae90857ec7f8ddb2dd847a0484cda87f0dee6e467126eb5929cc85d25"
                    }

                    response = requests.post(API_URL, data)
                    print(response.json())

                if len(self.btn_mobile):
                    API_URL = "http://api.wall.town/api/send-call-to-action"

                    data = {
                        "number" : self.number[i],
                        "urlbtn" : self.url_btn,
                        "callbtn" : self.btn_mobile,
                        "urlbtntext" : self.url_btn_name,
                        "callbtntext" : self.btn_mobile_name,

                        "instance" : "68e41486aaa1fc1e8a87f579f769eb6d274816bdce1577c4dbfcda1f18ff5cca",
                        "apikey" : "89579afae90857ec7f8ddb2dd847a0484cda87f0dee6e467126eb5929cc85d25"
                    }

                    response = requests.post(API_URL, data)
                    print(response.json())

                sleep(10)
            return "message success"
        except Exception as e:
            print(e)
            return "message fail"

