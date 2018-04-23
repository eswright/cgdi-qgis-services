# -*- coding: utf-8 -*-

#################################################################################

# Defines an object that contains attributes for all the necessary fields of a web service

# Created By: Nathan Torrence (nathan.torrence@canada.ca)

#################################################################################



class ServiceObject:
	
    def __init__(self, name, host, desc, serviceType, url, directory, layers):
        self.name = name
        self.host = host
        self.desc = desc
        self.serviceType = serviceType
        self.url = url
        self.directory = directory
        self.layers = layers
