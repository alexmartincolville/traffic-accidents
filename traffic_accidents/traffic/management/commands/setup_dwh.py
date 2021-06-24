import os
import pandas as pd
from django.conf import settings
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError
from traffic.utils import utils


class Command(BaseCommand):
    help = 'Reads files and content in the data folder.'

    def handle(self, *args, **options):
        """

        :return:
        """
        connection = connections['default']
        # Create db connection for df.to_sql
        engine = utils.get_db_engine(utils.get_db_uri(settings.DATABASES['default']))
        self.stdout.write('Preparing fact layer...')
        try:
            self.setup_fact(connection, engine)
        except CommandError:
            connection.close()
            raise CommandError('An error occurred on preparing fact layer.')
        # Close connection
        connection.close()

    def setup_fact(self, connection, engine):
        """

        :param connection:
        :return:
        """
        # Create cursor
        cursor = connection.cursor()
        # Get SQL file path
        sql_path = os.path.join(settings.BASE_DIR, 'queries', 'accident_information.sql')
        try:
            # Get SQL as string
            sql_file = open(sql_path)
            cursor.execute(sql_file.read())

            df = pd.DataFrame(cursor.fetchall())
            # Add column names
            df.columns = [i[0].lower() for i in cursor.description]
            df.to_sql('fact_accident_vehicle', engine, schema='dwh', if_exists='replace', index=False)

        except OperationalError:
            cursor.close()
            raise CommandError('Error on database cursor.')
        finally:
            cursor.close()