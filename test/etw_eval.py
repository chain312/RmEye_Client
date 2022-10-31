
import time
import etw
import requests
import json
import  re
class MyETW(etw.ETW):
    def __init__(self, event_callback):
        # define capture provider info
        providers = [etw.ProviderInfo('Some Provider', etw.GUID("{5770385F-C22A-43E0-BF4C-06F5698FFBD9}"))]
        super().__init__(providers=providers, event_callback=event_callback)

    def start(self):
        # do pre-capture setup
        self.do_capture_setup()
        super().start()

    def stop(self):
        super().stop()
        # do post-capture teardown
        self.do_capture_teardown()

    def do_capture_setup(self):
        # do whatever setup for capture here
        pass

    def do_capture_teardown(self):
        # do whatever for capture teardown here
        pass
def sent_server(data):
    url='http://127.0.0.1:5000/api/v1/process'
    repone= requests.post(url=url,data=data)
    print(repone.status_code)


def log_extracting(x):

    try:
        data={}
        regex = re.compile('RULE: (\S+)\)')
        data["Action"] = regex.findall(x["Task Name"])[0].lower()
        data["Data"]=x
        print(data["Action"])
        # sent_server(data)
        url='http://192.168.0.41:5000/api/v1/process'
        repone= requests.post(url=url,data=json.dumps(data))
        print(repone.status_code)
    except:
        print(x)


def my_capture():
    # instantiate class
    capture = MyETW(lambda x: log_extracting(x))
    # start capture
    capture.start()
    # wait some time to capture data
    # time.sleep(5)
    # stop capture
    # capture.stop()


if __name__ == '__main__':
    my_capture()