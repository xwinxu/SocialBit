from facepy import GraphAPI
import requests
import json


class FBRecog(object):

    API_URL = "https://www.facebook.com/photos/tagging/recognition/?dpr=1"

    def __init__(self, access_token, cookies, fb_dtsg):
        self.access_token = access_token
        self.cookies = cookies
        self.fb_dtsg = fb_dtsg
        self.headers = {'x_fb_background_state': '1',
                        'origin': 'https://www.facebook.com',
                        'accept-encoding': 'gzip, deflate, lzma',
                        'accept-language': 'en-US,en;q=0.8',
                        'user-agent': 'FBRecog/API',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'referer': 'https://www.facebook.com/',
                        'cookie': self.cookies,
                        'dnt': '1'}
        self.graph = GraphAPI(self.access_token)

    def _post_photo(self, path):
        try:
            # Uploading the picture to Facebook
            # 443796519442914/feed, 443796519442914/photos
            # retry=3,
            response = self.graph.post(path='443796519442914/photos', retry=0, source=open(path, 'rb'))
        except Exception as e:
            print(e)
            return -1
        else:
            return response['id']

    def _query_recognition_api(self, post_id):
        payload = []
        data = 'recognition_project=composer_facerec&photos[0]=' + post_id
        data += '&target&is_page=false&include_unrecognized_faceboxes=false&include_face_crop_src=true'
        data += '&include_recognized_user_profile_picture=true&include_low_confidence_recognitions=true'
        data += '&__a=1&fb_dtsg=' + self.fb_dtsg

        # Since the POST sometimes returns a blank array, retrying until a payload is obtained
        for i in range(20):
            response = requests.post(self.API_URL, data=data, headers=self.headers)
            payload = json.loads(response.text.replace('for (;;);', ''))['payload']
            if payload and "faceboxes" in payload[0] and payload[0]['faceboxes']:
                break

        return payload[0]['faceboxes']

    def recognize_raw(self, path):
        print('Post data to Facebook, please wait...')
        post_id = self._post_photo(path)
        result = None
        if post_id != -1:
            try:
                print("Querying Facebook, please wait...")
                result = self._query_recognition_api(post_id)
            except (KeyError, IndexError) as e:
                print("Unable to fetch details. API unresponsive. Please try again later.")
            except Exception as e:
                print(e)

        # Deleting the uploaded picture
        # print("Please wait. Cleaning up...")
        # delete gives all the errors b/c we don't have the access rights
        # not deleting will be good for demo, shows that everything is uploaded
        # self.graph.delete(path=post_id, retry=5)

        print("Finished.")

        return result

    def recognize(self, path):
        """Face recognition using Facebook's recognize method
            Args:
                path : file path of the photo to be processed
            Returns:
                result : array of recognitions with the name of recognized people
                         and the certainity of each recognition
        """
        faceboxes = self.recognize_raw(path)
        result = []
        for recog in faceboxes:
            name = recog['recognitions']
            if name:
                result.append({'name': name[0]['usabriser']['name'], 'certainity': name[0]['certainty']})
        return result
