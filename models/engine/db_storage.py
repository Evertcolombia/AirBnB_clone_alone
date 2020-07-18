#usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
import os


aux_classes = {
    'State': State, 'Place': Place, 'City': City,
    'Amenity': Amenity, 'Review': Review, 'User': User
}


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):
        """ Create a conection pipe and store in __engine
            use the environ variable to get that cnnection
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST"),
            os.environ.get("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        # if enviomenr is fort test deletes alss data Base mappers
        if os.environ.get("HBNB_ENV") == 'test':
            Base.drop_all(bind=self.__engine)


    def all(self, cls=None):
        """ Make a query to db based on cls, to bring all elements
            of this specific class or all elements en all class
            class are (table mappers)
        """
        if not self.__session:
            self.reload()

        items = {}

        if type(cls) == str:
            cls = aux_classes[cls]

        if cls:
            items = self.retrieve_items(cls)
        else:
            elements = {}
            for cl in aux_classes.values():
                elements = self.retrieve_items(cl)
                items = {**items, **elements}
        return items


    def retrieve_items(self, cls):
        """" Retrieve items from specific row on table db"""
        items = {}
        for row in self.__session.query(cls):
            key = "{}.{}".format(row.__class__.__name__, row.id)
            items[key] = row
        return items
    
    def new(self, obj):
        """ Create new object row on db """
        self.__session.add(obj)

    def save(self):
        """ sabe session objects on db"""
        self.__session.commit()

    def delete(self, obj=None):
        """ deletes an object to db"""
        if not self.__session:
            self.reload()
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ reload data and get Session """
        # create all tables in the db
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # create current db session from engine using register
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        self.__session.remove()

    def get(self, cls, id):
        """retrieve one object based on
            the class name and its ID"""
        if type(cls) == str:
            cls = aux_classes[cls]

        if cls and id:
            item = self.__session.query(cls).filter(cls.id == id).first()
            # for keywords epxresision for values thar are not primary key
            #item = self.__session().query(cls).filter_by(id = id).first()
            if item: return item
        return None

    def count(self, cls=None):
        """Returns the number of objects in storage matching
        the given class name."""
        count = 0
        if cls:
            if type(cls) == str and cls in aux_classes:
                cls = aux_classes[cls]
            count = self.__session.query(cls).count()
        else: 
            for cl in aux_classes.values():
                count += self.__session.query(cl).count()
        return count
