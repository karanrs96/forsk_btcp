# -*- coding: utf-8 -*-
"""
Created on Fri May 18 14:03:49 2018

@author: Karan
"""

from twython import Twython

twitter = Twython("Rrr8Lvpx6PHy5TRULGk6Id7Bm","GFvgXdZXBbCouOF0rIiL4XyQ3qIZ9ZjRZCTlVqtvubgrHTf821", "997356131205894145-SmSE2QcYhjF8vnQ2CKiOxsEUSFKTK05", "acGJEgxyih5pS38Gw1FLtbkyTljme18LD8RlegtXhTYii")

twitter.update_status(status="testing")
