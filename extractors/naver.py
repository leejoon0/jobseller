from requests import get
from bs4 import BeautifulSoup

def extract_keywords(keyword):
    base_url = "https://keywordmaster.net/키워드검색량조회/?keyword="
    base_url = "https://www.coupang.com/np/search?component=&q=키보드&channel=user"

    # response = get(f"{base_url}{keyword}")
    response = get(f"{base_url}")
    if response.status_code != 200:
        print('요청 오류')
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        search_keywords = soup.find_all(['table','tbody'], attrs={'id':'data'})

        # tmp = soup.find("table tbody tr", attrs={'id':'data'})
        # print(tmp)
        
        for keywd in search_keywords:
            rows = keywd.find_all('tr')
            rows.pop(0)
            rows.pop(0)
            for r in rows:
                title, val1, val2, val3, val4, val5, val6, val7, val8 = r.find_all('td')
                # print(title.string, val1.string, val2.string, val3.string, val4.string, val5.string, val6.string, val7.string, val8.string)
                keyword_data = {
                    'keyword': title.string,
                    'monthlySrhCountPC':val1.string,
                    'monthlySrhCountMobile':val2.string,
                    'monthlyClickCountPC':val3.string,
                    'monthlyClickCountMobile':val4.string,
                    # '':val5.string,
                    # '':val6.string,
                    'competition':val7.string,
                    'monthlyExt':val8.string,
                }

                results.append(keyword_data)
                
        return results
