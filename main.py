# _*_ coding: utf-8 _*_

from cmdb import create_app
from cmdb.models import db
from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
