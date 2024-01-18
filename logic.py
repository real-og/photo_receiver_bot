from webdav3.client import Client
import os


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


def upload_all_files(dir_path_global):
    client.mkdir('Saw_bot')
    client.mkdir(f'Saw_bot/{dir_path_global}')
    files_names = []

    try:
        for file_name in os.listdir('buffer_files'):
            files_names.append('buffer_files/' + file_name)
    except:
        pass

    try:
        for file_name in os.listdir('buffer_files/documents'):
            files_names.append('buffer_files/documents/' + file_name)
    except:
        pass

    for file_name in files_names:
        old_name = file_name.split('/')[-1]
        client.upload_async(f'{GLOBAL_FOLDER}/{dir_path_global}/{old_name}', file_name)
