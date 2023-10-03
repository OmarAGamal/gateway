"""Platform for Gateway integration."""
from __future__ import annotations
# import asyncore
# import socket
from homeassistant.components.gateway import (
    GatewayDeviceClass,
    GatewayEntity,
    GatewayStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
homeassistant.components.gateway.GatewayEntity
GatewayDeviceClass.TEMPERATURE
# ServerActive = True
# Serverip = '185.222.242.249'
# Serverport = 5029
def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the gateway platform."""
    # add_entities([ExampleSensor()])


# class EchoHandler(asyncore.dispatcher_with_send):

#     def handle_read(self):
#         data = self.recv(8192)
#         if data:
#             try:
#                print("data recieved")
#             except :
#                 print("data not recieved")


# class EchoServer(asyncore.dispatcher):

#     def __init__(self, host, port):
#         asyncore.dispatcher.__init__(self)
#         self.create_socket()
#         self.set_reuse_addr()
#         self.bind((host, port))
#         self.listen(5)

#     def handle_accepted(self, sock, addr):
#         print('Incoming connection from %s' % repr(addr))
#         handler = EchoHandler(sock)


# server = EchoServer('', 2000)
# asyncore.loop()
