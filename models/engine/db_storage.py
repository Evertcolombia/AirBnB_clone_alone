from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
import os


class DBStorage:

    __engine = None
    __session = None

    def __init__(self):

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get(HBNB_MYSQL_USER),
            os.environ.get(HBNB_MYSQL_PWD),
            os.environ.get(HBNB_MYSQL_HOST),
            os.environ.get(HBNB_MYSQL_DB)),
            pool_pre_ping = True)

        if os.environ.get("HBNB_ENV") == 'test'
            Base.drop_all(bind=self.__engine)


    def all(self, cls=None):
        """ Make a query to db based on cls, to bring all elements
            of this specific class or all elements en all class
            class are (table mappers)
        """
        items = {}
        aux_classes = {
            'State': State, 'Place': Place, 'City': City,
            'Amenity': Amenity, 'Review': Review, 'User': User
        }

        if cls:
            items = self.retrieve_items(aux_classes, cls)
            #for row in self.__session.query(aux_classes[cls])
                #key = "{}.{}".format(row.__class__.__name__, row.id)
                    #items[key] = row
        else:
            for cl in aux_classes:
                items += self.retrieve_items(aux_classes, cl)
                #for row in self.session.query(aux_classes[cl]):
                    #key = "{}.{}".format(row.__class__.name__, row.id)
                    #items[key] = row
        return items


    def retrieve_items(self, aux_classes, cls):
        items = {}
        for row in self.__session.query(aux_classes[cls]):
            key = "{}.{}".format(row.__class__.__name__)
            items[key] = row
        return items
    
    def new(self, obj):
        self.__session.add(obj)
        self.save()

    def save(self):
        self.__session.commit()    

