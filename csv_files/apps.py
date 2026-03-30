from django.apps import AppConfig
from django.db.models.signals import post_save



from csv_files.lib import make_file_readonly_callback

class CsvFilesConfig(AppConfig):
    name = 'csv_files'

    def ready(self):
        from csv_files.models import CsvFile
        post_save.connect(make_file_readonly_callback, sender=CsvFile)