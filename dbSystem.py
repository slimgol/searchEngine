from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:',echo=True)

Session = sessionmaker(bind=engine)
session = Session()

baseClassInstance = declarative_base()

class Urls(baseClassInstance):#Inherit base class.
    __tablename__ = 'urls'#Set attribute of the base class.

    '''Define field to store the url. Note that each url identifies a unique web resurce, thus, we can use this as the primary key for this table.'''
    urlName = Column(String(200),primary_key=True)

    def __repr__(self):
        return self.urlName
    
baseClassInstance.metadata.create_all(engine)

session.add(Urls(urlName='https://en.wikipedia.org/wiki/Self-driving_car'))

session.commit()

res = session.query(Urls).all()

for r in res:
    print(r)
    
