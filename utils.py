# utilities 

import platformdirs

from platformdirs import PlatformDirs, AppDirs, user_documents_dir, user_data_dir, user_data_path
app_name = 'fileDownloader'
platform = PlatformDirs(appname=app_name)
documents = user_documents_dir()
data_path = platform.site_data_path
data_dir = user_data_dir(appname=app_name)
#print(f'Dir=={data_dir} Path=={data_path}')

resolution = ['1080p','720p','480p','360p','240p']
tag = [96, 95, 83, 93, 92]
d = {}
end = len(tag)
start  = 0

def check(start, end):
	if start == end:
		print('complete')
	else:
		print('Not yet')

from plyer import storagepath

app = storagepath.get_application_dir()
downloads = storagepath.get_downloads_dir()
print(f'app == {app}')
print(f'downloads == {downloads}')




