import os
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from traffic.utils import utils


class Command(BaseCommand):
    help = 'Reads files and content in the data folder.'

    def handle(self, *args, **options):
        """

        :return:
        """
        # Create db connection for df.to_sql
        engine = utils.get_db_engine(utils.get_db_uri(settings.DATABASES['default']))
        self.stdout.write('Preparing input layer...')
        try:
            self.setup_input(engine)
        except CommandError:
            engine.close()
            raise CommandError('An error occurred on inputting files from CSV.')
        # Close db engine
        engine.close()

    def setup_input(self, engine):
        """

        :param engine:
        :return:
        """
        data_path = os.path.join(settings.BASE_DIR, 'data')
        for filename in os.listdir(data_path):
            try:
                df = pd.read_csv(os.path.join(data_path, filename))
                df.to_sql('input_{}'.format(filename.lower().split('.')[0]), engine, schema='input',
                          if_exists='fail', index=False)
            except Exception as e:
                raise CommandError('Error getting file "%s".' % filename)

            self.stdout.write(self.style.SUCCESS('Successfully uploaded CSV "%s".' % filename))