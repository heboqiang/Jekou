#!/use/bin/env python
#coding:utf-8

#Author:WuYa

import  unittest
import  json
from base.method import Method,IsContent
from page.laGou import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson

class LaGou(unittest.TestCase):
	def setUp(self):
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()

	def statusCode(self,r):
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['result_code'], 200)

	def isContent(self,r,row):
		self.statusCode(r=r)
		self.assertTrue(self.p.isContent(row=row,str2=r.text))

	def test_laGou_001(self):
		'''测试1'''
		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(1))
		print ("test_laGou_001 is:", r.text)
		self.isContent(r=r,row=1)
		self.execl.writeResult(1,'pass')

