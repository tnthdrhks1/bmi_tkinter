import random

gok_list = {"쌀밥" : 70, "보리밥" : 70, "현미밥" : 70, "쌀죽" : 140, "식빵" : 35}
name = list(gok_list.keys())

ran = random.randrange(0,len(name))
print(name[ran]) #음식이름
print(gok_list['{0}'.format(name[ran])]) #음식량

# print(gok_list['{0}'.format(name[2])])
# gok_list = [{"쌀밥" : 70}, {"보리밥" : 70}, {"현미밥" : 70}, {"쌀죽" : 140}, {"식빵" : 35}]
# print(gok_list["쌀밥"])