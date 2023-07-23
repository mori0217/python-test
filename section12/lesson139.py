import sqlalchemy
from sqlalchemy.ext import declarative
from sqlalchemy import orm

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# engine = sqlalchemy.create_engine('sqlite:///section12/lesson139.sqlite', echo=True)
# engine = sqlalchemy.create_engine('mysql+pymysql://root:password@localhost/test_database_sqlalchemy', echo=True)

Base = declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)

Session = orm.sessionmaker(bind=engine)
session = Session()

person1 = Person(name='Mike')
session.add(person1)
person2 = Person(name='Nancy')
session.add(person2)
person3 = Person(name='Jun')
session.add(person3)
session.commit()

person4 = session.query(Person).filter_by(name='Mike').first()
person4.name = 'Michel'
session.add(person4)
session.commit()

person5 = session.query(Person).filter_by(name='Nancy').first()
session.delete(person5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
