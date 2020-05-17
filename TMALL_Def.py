from urllib3 import *
import _json
import re
from bs4 import BeautifulSoup
from Spider_Def import Read_Headers
headers = Read_Headers('head_tm.txt')
disable_warnings()
http = PoolManager()
def getProductIdList():
   url = 'https://list.tmall.com/search_product.htm?start_price=3800&search_condition=48&sort=d&style=g&from=.list.pc_1_searchbutton&q=mate30&shopType=any#J_Filter'
   # url为搜索mate30排序和筛选后的链接
   r = http.request('GET',url,headers=headers)#将url的内容读取到r中
   # print(r.data)
   c = r.data.decode('GB18030')#将r中的内容通过GB18030进行解码
   # print(c)
   soup = BeautifulSoup(c,'lxml')#运用bs4分析c中内容
   data_id_list = []
   div_product = soup.find_all('div',class_='product')#找到所有的div并且class=product。将div中class=product的内容提取出来
   for data_id in div_product:
       data_id_list.append(data_id.attrs['data-id'])# 把所有div中的data-id提取出来
   # print(data_id_list)
   return_id_list = []
   for item in data_id_list:
       url = 'https://detail.tmall.com/item.htm?id=' + item
       r = http.request('GET',url,headers=headers)
       r = r.data.decode('GB18030')
       soup = BeautifulSoup(r,'lxml')
       item_name = soup.find('div',class_='tb-detail-hd').text
       if re.match('.*[Mm][Aa][Tt][Ee]\s*30.*',item_name.strip()):
          return_id_list.append(item)
   return return_id_list

def getJSONDetail(url,itemId,currentPage):
    re_result = re.match('.+itemId=(.+)&spuId.+&currentPage=(.+)&append.+callback=(.+)$',url).groups()
    print(re_result)



if __name__ == '__main__':
   # print(getProductIdList())
   url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=602918373522&spuId=1356405284&sellerId=2838892713&order=3&currentPage=3&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvmvvxvxwvUvCkvvvvvjiPn2cOtjlHRLqyljnEPmPZ6jE2P2d9zjtVPszU0j3RRphvCvvvvvmCvpvZ7Dly4E5w7Di4HFj5PV3f%2Fxulz1VrvpvEvvsRkmUkvbE4dphvmpvW6IFf0QmAL2yCvvpvvvvvCQhvCli4zYMwTGTrvpvEvvk3kVDivjBadphvmpvU8g85iQvGF46Cvvyv2Cum5igvPbmrvpvEvvsBvYPLvvQHiQhvCvvv9UUPvpvhvv2MMqyCvm9vvvvvphvvvvvv9JHvpvQFvvm2phCvhRvvvUnvphvppvvv96CvpCCvuphvmvvv92D3WwYqkphvC99vvOCgopyCvhQU7CZvCsfv%2BneYr2E9ZRAn3w0AhjECTWex6fItb9TxfJCl5dvfNezUacZ7%2B3%2BiaNohD46wjLVDYExrV4tML%2BFptRk4VzX2%2BneYiLUpvphvC9vhvvCvp2yCvvpvvvvv3QhvCvvhvvmrvpvEvvAdvGznvvsDdphvmpvW09eSdQ2e59%3D%3D&needFold=0&_ksTS=1589696901222_776&callback=jsonp777'
   itemId = '602918373522'

   getJSONDetail(url, itemId, 1)