import vk
import time
# ID Пользователя
userId = 43642612
# Тематика
theme = 'Юмор'
access_token = '9a5e6d423bc48beb2c516d5fd1541459d64d8d1def31db2ed947ba08998aca25825325dac4cb32d442b7e'
session = vk.Session(access_token = access_token)
vk_api = vk.API(session)
version = '5.00'
# Наш результат
map = dict()


def getFriends():
    friends = vk_api.friends.get(user_id = userId, v = version)
    return friends

def getGroups(id):
    groups = vk_api.groups.get(user_id = id, v = version)
    time.sleep(0.3)
    return groups

def getActivity(groupId):
    activity = vk_api.groups.getById(group_id = groupId, v = version, fields = 'activity')
    time.sleep(0.3)
    return activity


def mainAction():
    # Получение списка друзей
    friends = getFriends()
    count = 0
    for i in range(len(friends['items'])):
        friendId = friends['items'][i]
        map[friendId] = 0
        # Получение списка групп у определенного пользователя
        groups = getGroups(friendId)
        for i in range(len(groups['items'])):
            groupId = groups['items'][i]
            # Получение тематики группы
            groupInfo = getActivity(groupId)[0]
            if 'activity' in groupInfo:
                activity = getActivity(groupId)[0]['activity']
                if activity == theme:
                    map[friendId] = map[friendId]+1
                    count = count + 1
                    # Вывод
                    print(count)
                    print(map)


def main():
    mainAction()
# Start
main()
print('The program has finished working')
# End