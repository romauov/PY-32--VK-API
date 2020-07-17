import requests
from pprint import pprint

access_token = ''

class VK_user:

    def __init__(self, id):
        self.id = id

    def get_friends_list(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token' : access_token,
                'v' : 5.21,
                'user_id' : self.id
            }
        )
        return response.json()


    def get_id(self):
        return self.id

    def __str__(self):
        return 'https://vk.com/id' + str(self.id)

# class VK_friends:
#
#     def __init__(self, id):
#         self.id = id
#         self.friends_list = []
#         response = requests.get(
#             'https://api.vk.com/method/friends.get',
#             params={
#                 'access_token': access_token,
#                 'v': 5.21,
#                 'user_id': self.id
#             }
#         )
#         friends = response.json()['response']['items']
#         for friend in friends:
#             self.friends_list.append(VK_user(friend))
#
#     def get_friends_ids_list(self):
#         self.ids_list = []
#         for friend in self.friends_list:
#             self.ids_list.append(friend.get_id())
#         return self.ids_list
#
#     def get_friends(self):
#         return self.friends_list
#
#
# def common_friends(user1, user2):
#
#     set1 = user1.get_friends()
#     set2 = user2.get_friends()
#     print(set1)
#     print(set2)
#     # common = set(user1.get_friends()) & set(user2.get_friends())
#     # print(common)
#     # print(len(common))
#     return






romauov = VK_user(194208214)
skory = VK_user(10443102)
yourstruly = VK_user(8462865)

skory_friends = skory.get_friends_list()['response']['items']
YT_friends = yourstruly.get_friends_list()['response']['items']
common_friends = set(skory_friends) & set(YT_friends)

common = []
for friend in common_friends:
    common.append(VK_user(friend))

print(romauov)
print(common)
print(len(common))
