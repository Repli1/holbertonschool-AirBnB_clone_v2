#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysqlmysqldb://{}:{}@{}/{}'.format
                (getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                 getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                 pool_pre_ping=True)
        if getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if cls is None:
            class_list = [User, State, City, Amenity, Place, Review]
            obj_dict = {}
            for element in class_list:
                query = self.__session.query(element)
                for obj in query:
                    obj_dict[f"{type(obj).__name__}.{obj.id}"] = obj

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is None:
            pass
        else:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expireon_commit=False)
        Session = scoped_Session(session)
        self.__session = Session()
