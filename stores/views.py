from django.shortcuts import render
from rest_framework import generics
import json
from models import StoreMapping,ArticleMapping
from django.core.exceptions import ObjectDoesNotExist

class StoreInfo(generics.ListCreateAPIView):
    store_model = StoreMapping
    article_model = ArticleMapping


    def process_data(self,file_data):
        file_list=[]
        for data in file_data:
            store_id=self.store_obj(data)
            prod_id = self.prod_obj(data)
            file_dict={'store_name':store_id.store_name,
                              'product_name':prod_id.name,
                              'price':prod_id.price,'avail':prod_id.availabilty,
                              'stock':prod_id.stock
                              }
            file_list.append(file_dict)
        print file_list        
        return file_list

    def store_obj(self,data):
        try:
            return self.store_model.objects.get(merchant_id=data['merchant_id']).store
        except ObjectDoesNotExist:
            print "Object doesn't exist"
            with open('/home/bharat/data1.json','w') as file: 
                return file.write(data)

    def prod_obj(self,data):
        try:
            return self.article_model.objects.get(article_id=data['article_id']).product
        except ObjectDoesNotExist:
            print "Object doesn't exist"
            with open('/home/bharat/data1.json','w') as file: 
                return file.write(data)
            
    def process(self,arg):
        with open(arg,'r') as json_file:
            file_data = json.load(json_file)
            return self.process_data(file_data)
    
    def get(self, request, *args, **kwargs):
        get_param = request.GET.get('data',None)
        return self.process(get_param)
        
    