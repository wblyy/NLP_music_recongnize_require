# -*- coding: utf-8 -*- 
import urllib2
import urllib
from mydb import NLPdb
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')
word_dict={'a':'adjective',
		   'b':'other_noun_modifier',	
		   'c':'conjunction',
		   'd':'adverb',
		   'e':'exclamation',
		   'g':'morpheme',
		   'h':'prefix',
		   'i':'idiom',
		   'j':'abbreviation',
		   'k':'suffix',
		   'm':'number',
		   'n':'general_noun',
		   'nd':'direction_noun',
		   'nh':'person_name',
		   'ni':'organization_name',
		   'nl':'location_noun',
		   'ns':'geographical_name',
		   'nt':'temporal_noun',
		   'nz':'other_proper_noun',
		   'o':'onomatopoeia',
		   'p':'preposition',
		   'q':'quantity',
		   'r':'pronoun',
		   'u':'auxiliary',
		   'v':'verb',
		   'wp':'punctuation',
		   'ws':'foreign_words',
		   'x':'non_lexeme',		
}

NLP=NLPdb()
sentences=NLP.get_sentence('无',1)
for sentence in sentences:
	try:
	
		sentence_url='http://ltpapi.voicecloud.cn/analysis/?api_key=62S5e8g1Rwab5wIgSIOyeUBUpqkXIjLVKo7GlxDz&text='+sentence[0]+'&pattern=all&format=json'
		msg=urllib2.urlopen(sentence_url).read()
	#print msg.decode('utf-8')
		json_info=json.loads(msg)
		#print json_info
	#print json_info[1]["pos"]
	#print json_info
	#pos = json_info.get('pos')
		for info in json_info[0][0]:
			pos= word_dict.get(info["pos"])
			#print pos
			cont= info["cont"].encode('utf-8')#.decode('utf-8')
			#cont='是'
			print pos,cont.encode('gbk')
			#if 'verb'==pos and ('是'==cont or cont == '问' or cont == '叫' or cont == '有' or cont == '求' or cont == '知道'):
			#	print '去除废词'.encode('gbk')
			#	continue

			NLP.update_sentence_pos(sentence[0],pos,cont)
	#print json.dumps(json_info,sort_keys=True,indent=4)  
	except Exception, e:
		print e
