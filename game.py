import json
def set_charact(name):
    character = {
      "name": name,
      "level": 1,
      "items": ["애교", "SOS요청" ],
      "skill": ["수저사용", "손을 사용"]
    }
    with open('static/save.txt', 'w', encoding='utf-8') as f:
       json.dump(character, f , ensure_ascii = False, indent=4)
    #print("{0}님 놀러와 동물의 세계에 오신것을 환영합니다!! {0}님은 아기코알라를 배정받게 되었습니다. (Lv {1}) 로딩중...". format(character["name"], character["level"]))
    return character

    
def save_game(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()