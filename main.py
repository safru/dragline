#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from dragline.runner import main
# from dragline.parser import HtmlParser
# from dragline.http import Request, RequestError
# from . import settings
# from .items import *
# from dragline.http import Request
import requests
import json
import os
import csv
import pprint

class Spider:

		def __init__(self):
			self.parse()
