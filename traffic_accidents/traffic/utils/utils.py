from sqlalchemy import create_engine


def get_db_uri(db):
    return ''.join(['postgresql://', db['USER'], ':', db['PASSWORD'], '@', db['HOST'], ':', str(db['PORT']), '/',
                    db['NAME']])


def get_db_engine(uri):
    return create_engine(uri).connect()
