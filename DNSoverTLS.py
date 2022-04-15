import socket
import threading
import ssl
import binascii
import struct
from logger import logger

def dnsquery(dns_query):
    pre_length = "\x00"+chr(len(dns_query))
    _query = pre_length + dns_query
    return _query