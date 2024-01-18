from webdav3.client import Client
import os
import shutil
import random

CLOUD_NAME = str(os.environ.get('CLOUD_NAME'))
CLOUD_PASSWORD = str(os.environ.get('CLOUD_PASSWORD'))
CLOUD_EMAIL = str(os.environ.get('CLOUD_EMAIL'))
GLOBAL_FOLDER=str(os.environ.get('GLOBAL_FOLDER'))


data = {
 'webdav_hostname': CLOUD_NAME,
 'webdav_login':    CLOUD_EMAIL,
 'webdav_password': CLOUD_PASSWORD
}
client = Client(data)

def move_files(source_folder, destination_folder):
    files = os.listdir(source_folder)
    for file_name in files:
        
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)

        shutil.move(source_file, destination_file)


def upload_all_files(dir_path_global):
    move_files('buffer_files/documents', 'buffer_files')
    if not client.check('Saw_bot'):
        client.mkdir('Saw_bot')
    if not client.check(f'{GLOBAL_FOLDER}/{dir_path_global}'):
        client.upload_sync(f'{GLOBAL_FOLDER}/{dir_path_global}', 'buffer_files')
    else:
        client.upload_sync(f'{GLOBAL_FOLDER}/{dir_path_global}-{random.randint(0, 1000000)}', 'buffer_files')
    try:
        shutil.rmtree('buffer_files')
    except:
        pass
    try:
        os.mkdir('buffer_files')
        os.mkdir('buffer_files/documents')
    except:
        pass

