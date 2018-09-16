#from pprint import pprint
#from fbrecog import recognize
# changed the init file into fbrecogg
from fbrecogg import FBRecog
path = '' # Insert your image file path here
#path2 = '2.jpg' # Insert your image ddfile path here
access_token = '' # Insert the access token for project
cookies = '' # Insert the cookies ID from inspecting network on facebook
fb_dtsg = '' # Insert the fb_dtsg parameter obtained from Form Data here.
# Instantiate the recog class
recog = FBRecog(access_token, cookies, fb_dtsg)
# Recog class can be used multiple times with different paths
print(recog.recognize(path))
#print(recog.recognize(path2))

# Call recognize_raw to get more info about the faces detected, including their positions
#pprint(recog.recognize_raw(path), indent=2)
