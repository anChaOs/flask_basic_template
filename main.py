"""
    csw     flask车卫士

    2014.05.13 xiongchen
"""

import os
# import gevent.monkey

# gevent.monkey.patch_all()

from app import create_app
    
print("main.py")
cfg = os.getenv('FLASK_CONFIG') or 'default'
print(cfg)

main = create_app(cfg)
