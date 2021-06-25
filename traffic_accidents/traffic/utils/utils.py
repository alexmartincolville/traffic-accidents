from sqlalchemy import create_engine, types


def get_db_uri(db):
    return ''.join(['postgresql://', db['USER'], ':', db['PASSWORD'], '@', db['HOST'], ':', str(db['PORT']), '/',
                    db['NAME']])


def get_db_engine(uri):
    return create_engine(uri).connect()


def get_column_types(df):

    type_dict = {}
    for i, j in zip(df.columns, df.dtypes):
        if "object" in str(j):
            type_dict.update({i: types.TEXT()})
        if "datetime" in str(j):
            type_dict.update({i: types.DateTime()})
        if "float" in str(j):
            type_dict.update({i: types.Float(precision=3, asdecimal=True)})
        if "int" in str(j):
            type_dict.update({i: types.INT()})

    return type_dict
