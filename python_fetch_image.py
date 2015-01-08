# encoding : utf-8
# for python3
import urllib.request
import os.path
import pyquery as pq
import requests

def download(url, folderName):
	if not os.path.exists(folderName):
		print (folderName + "フォルダを作成しました")
		os.mkdir(folderName)
	save_path = './'+folderName+'/'
	src= urllib.request.urlopen(url)
	html = src.read()
	query = pq.PyQuery(html)
	
	results = []
	for img_tag in query('img'):
		if 'jpg' or 'png' in img_tag:
			img_url = query(img_tag).attr('src')
			results.append(img_url)
			print (os.path.basename(img_url))
			with open (save_path + os.path.basename(img_url), 'wb') as f:
				raw = requests.get(img_url).content
				f.write(raw)
	
	print (results[1])
if __name__ == '__main__':
	print ("写真を取得したいサイトのURLを入力してください")
	input_url = input('>>>  ')
	target_url = input_url
	
	print ("保存先フォルダ名を入力してください（※存在しない場合は新規作成されます）")
	input_folderName = input('>>>  ')
	target_folderName = input_folderName
	
	download(target_url, target_folderName)