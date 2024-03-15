import googleapiclient.discovery
from pprint import pprint
import streamlit as st


ytApiKey = 'AIzaSyCpgtmHkUG_2PT4_PQFwFtKW-AbE3Ul8xA'
scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_service_name = "youtube"
api_version = "v3"
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=ytApiKey)


chId = st.text_input('Channel ID')
if chId and st.button('Get Details'):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=chId
    )
    response = request.execute()
    st.write(response)

chDetails = {
    'chId': chId,
    'chName': '',
    'chDesc': '',
    'usr': '',
    'thumbnail': '',
    'country': '',
    'videosId': '',
    'viewCount': '',
    'subCount': '',
    'vidCount': ''
}