import eel
import requests

eel.init('web')

@eel.expose
def test(singer,song):
    url = 'https://api.lyrics.ovh/v1/'+singer+'/'+song

    website = requests.get(url)

    data = website.json()

    lyrics = data['lyrics']

    eel.setLyrics(lyrics)

eel.start('main.html',size=(1300,760))
