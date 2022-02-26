from __future__ import unicode_literals
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
import json 

from django.views.decorators.csrf import csrf_exempt
from .models import FoodOrder

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def fetch_data_db(item_name):
    logger.info('Inside the fetch_data_db function......')
    # This is our data select query.
    food_data = FoodOrder.objects.filter(item=item_name)
    for tbl_value in food_data.values():
        return tbl_value

def insert_data_db(item_name, item_category, item_price):
    logger.info('Inside the insert_data_db function.......')
    # This is our data insert query.
    rest = FoodOrder(category=item_category, item=item_name, price=str(item_price))
    rest.save()
    return 1

## It is used for inserting the data through user request.
@csrf_exempt
def post_req(request):
    item_name = request.POST.get('Item_name','')
    item_category = request.POST.get('Item_category','')
    item_price = request.POST.get('Item_price','')

    resp = {}
    # This loop will check data is send in key or not.
    if item_name == '' or item_category=='' or item_price=='':
        resp['status'] = 'Failed'
        resp['status_code']='400'
        resp['result']= 'None'
    else:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = {}
        rest_data = insert_data_db(item_name, item_category, item_price)

        if rest_data:
            resp['data'] = 'Data is added successfully.'
        else:
            resp['status'] = 'Failed'
            resp['status_code']='400'
            resp['result']= 'None'
    
    return HttpResponse(json.dumps(resp), content_type='application/json')


## It is used for getting the data from the database through user request.
def get_req(request):
    item_name = request.GET.get('Item_name','') 
    resp = {}
    # It will check the item_name value.
    if item_name == '':
        resp['status'] = 'Failed' 
        resp['status_code'] = '400'
        resp['result'] = 'None'
    else:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = {}
        item_details = fetch_data_db(item_name)
        # If item_details not black than if part will run. if item_details:
        resp['data'] = item_details
        # If rest_data is black than else part will run. else:
        resp['data'] = "Data is not Available"
    return HttpResponse(json.dumps(resp), content_type = 'application/ json')



