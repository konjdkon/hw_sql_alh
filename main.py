import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Publisher, Shop, Stock, Sale


if __name__ == "__main__":
    DSN = "postgresql://postgres:______@localhost:5432/net_db_1"
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    '''
    with open('tests_data.json', 'r') as fd:
        data = json.load(fd)
    
    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
    session.commit()
    '''

    pb_id = int(input('Введите id издателя' + '\n'))
    query = session.query(Publisher).filter(Publisher.id == pb_id)
    for c in query.all():
        print(c)
