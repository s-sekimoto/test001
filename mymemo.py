# -*- coding: utf-8 -*-

import os
import feedparser

url = "https://alas.aws.amazon.com/alas.rss"
base_path = "./"

old_feed_file = open(base_path + "alas_old.txt")
old_feed_list = feedparser.parse(old_feed_file.read())
new_feed_file = open(base_path + "alas.txt")
new_feed_list = feedparser.parse(new_feed_file.read())

target_package = ['kernel', 'mysql57', 'php71', 'gcc', 'httpd24']
target_severity = ['critical', 'important']
target_email = ['']

# TODO add try exception
# TODO get new feed file
# if wget error 

i = 0
for entry in new_feed_list.entries:
	new_title = entry.title
	old_title = old_feed_list.entries[0].title
	if new_title == old_title:
		break
	
	print(i)
	
	#if severity level match, add msg array
	new_parsed_title = parsetitle(new_title)
	if new_parsed_title[1] in target_severity:
		#print(new_parsed_title[2])
		for package in target_package:
			#print(package)
			#new_parsed_title[2]
			#print('affected!!')
			if package in new_parsed_title[2]:
				print(package)
				print(new_parsed_title[2])
	#print (new_title)
	print(new_parsed_title)
	i += 1 

	if i > 10:
		break

#if msg array.length, send email

def parsetitle(titletext):
	title_list = []
	delimiter01_index = titletext.find(' (')
	delimiter02_index = titletext.find('): ')
	
	title_list.append(titletext[0:delimiter01_index])
	title_list.append(titletext[delimiter01_index+2:delimiter02_index])
	title_list.append(titletext[delimiter02_index+3:])
	return title_list
	#print s[-1:n-1+m]  # 'This'
