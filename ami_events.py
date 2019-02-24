from asterisk.ami import AMIClient
from asterisk.ami import EventListener
import time

class RegistryEventListener(EventListener):

    def on_Registry(event, **kwargs):
        print('Registry Event', event)

class AllEventListener(EventListener):

    def on_event(event, **kwargs):
        print('Event', event)

client = AMIClient(address='192.168.66.104')
client.login(username='beagle', secret='password')
#client.add_event_listener(RegistryEventListener())
#client.add_event_listener(AllEventListener())

client.logoff()
time.sleep(100)
