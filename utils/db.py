from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = SQLAlchemy()
ma = Marshmallow()

engine = create_engine('postgresql://postgres:zeekit@localhost:5432/zeekit')
Session = sessionmaker(bind=engine)

session = Session()


Base = automap_base()
Base.prepare(engine, reflect=True)
