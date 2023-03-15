from yandex_music import Client


def getListTrackId(playlist):
    listId = []
    for i in range(0,len(playlist)):
        listId.append(playlist[i].id )
    return listId

def getplaylist(user_id, playlist_id):
    return client.users_playlists(playlist_id, user_id=user_id)

def trackInList(id_track, listId):
    if int(id_track) in listId:
        return True
    else:
        return False

def getTrackFromPlaylist(playlist,idList,id):
    return (playlist[idList.index(id)].fetch_track())



token="ENTER_TOKEN"
client = Client(token).init()
my_id = client.me.account.login
playlist=getplaylist(my_id,3).fetch_tracks()
listIds=getListTrackId(playlist)
for id in listIds:
    track=getTrackFromPlaylist(playlist,listIds,id)
    print(f"{track.artists_name()} - {track.title}")