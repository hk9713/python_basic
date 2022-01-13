import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("ul",{"class":"pagination-list"})

    links = pagination.find_all('span')
    pages = []
    for link in links[:-2]:
        pages.append(int(link.text))
    max_page = (pages[-1])
    return max_page

def extract_job(html):
    title = html.select_one('.jobTitle>span').string
    company = html.find("span",{"class":"companyName"}).text
    location = html.select_one("pre > div").text
    job_id = html.parent['data-jk']
    return {'title':title,
            'company':company,
            'locaion':location,
            'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"
            }
    
def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"스크래핑 중... page..{page}..")
        result = requests.get(f"{URL}&start={page*LIMIT}")

        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"slider_container"})

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs