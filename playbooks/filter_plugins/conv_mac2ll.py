#!/usr/local/bin/python

def mac2ll(mac):
    mac = mac.split(":")
    mac.insert(3,'fe')
    mac.insert(3,'ff')
    mac[0] = str(int(mac[0]) ^ 6)
    return "fe80::%s:%s:%s:%s" % ("".join(mac[0:2]),"".join(mac[2:4]),"".join(mac[4:6]),"".join(mac[6:8]))


class FilterModule(object):
    ''' Ansible network jinja2 filters '''
    def filters(self):
        return {
            'mac2ll': mac2ll
            }
