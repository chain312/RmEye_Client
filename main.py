
import time
import etw


def some_func():
    # define capture provider info
    providers = [etw.ProviderInfo('Some Provider', etw.GUID("{1EDEEE53-0AFE-4609-B846-D8C0B2075B1F}"))]
    # create instance of ETW class
    job= etw.ETW(providers=providers, event_callback=lambda x: print(x))
    # start capture
    job.start()

    # wait some time
    time.sleep(5)

    # stop capture
    job.stop()
if __name__ == '__main__':
    some_func()