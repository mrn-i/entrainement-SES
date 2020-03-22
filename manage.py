#!/usr/bin/env python3

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from linear_app.views import app 
from linear_app.models import db 


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 5000), host='0.0.0.0')
    manager.run()
