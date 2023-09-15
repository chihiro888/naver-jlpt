import requests
import urllib.parse
import time
import json

for level in range(5, 6):
    result_list = []
    min_page = 1

    if level == 5:
        max_page = 76
    elif level == 4:
        max_page = 105
    elif level == 3:
        max_page = 156
    elif level == 2:
        max_page = 266
    elif level == 1:
        max_page = 326

    for page in range(min_page, max_page):
        # 요청할 URL
        url = f"https://ja.dict.naver.com/api/jako/getJLPTList?level={level}&part=%EC%A0%84%EC%B2%B4&page={page}"

        # GET 요청 보내기
        response = requests.get(url)

        # 응답 데이터 출력
        if response.status_code == 200:
            # 응답 데이터를 JSON 형식으로 파싱하여 출력
            data = response.json()
            m_items = data['m_items']
            for item in m_items:
                means = item['means']
                level = item['level']
                parts = item['parts']
                pron = item['pron']
                entry = urllib.parse.unquote(item['entry'])

                print(level)
                print(parts)
                print(means)
                print(pron)
                print(entry)
                print('----------------------------')

                result = {
                    'level': level,
                    'parts': parts,
                    'means': means,
                    'pron': pron,
                    'entry': entry,
                }
                result_list.append(result)
        else:
            print("요청이 실패하였습니다. 상태 코드:", response.status_code)

        time.sleep(0.3)

    with open(f'jlpt_{level}.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_list, json_file, indent="\t", ensure_ascii=False)