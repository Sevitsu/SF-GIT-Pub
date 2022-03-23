import json
with open('json_example_QAP.json', encoding='utf8') as f:
    templates = json.load(f)
def checkint(item):
    return isinstance(item, int)
def checkstr(item):
    return isinstance(item, str)
def checkbool(item):
    return isinstance(item, bool)
def checkurl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False
def checkstrvalue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False
def Errorlog(item, value, string):
    Error.append({item: f'{value}, {string}'})
listofitems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url', 'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str', 'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool', 'detectedCorruption': 'bool', 'firstInSession': 'bool'}
Error = []
for items in templates:
    for item in items:
        if item in listofitems:
            if listofitems[item] == 'int':
                if not checkint(items[item]):
                    Errorlog(item, items[item], f'expected type {listofitems[item]}')
            elif listofitems[item] == 'str':
                if not checkstr(items[item]):
                    Errorlog(item, items[item], f'expected type {listofitems[item]}')
            elif listofitems[item] == 'bool':
                if not checkbool(items[item]):
                    Errorlog(item, items[item], f'expected type {listofitems[item]}')
            elif listofitems[item] == 'url':
                if not checkurl(items[item]):
                    Errorlog(item, items[item], f'expected type {listofitems[item]}')
            elif listofitems[item] == 'val':
                if not checkstrvalue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    Errorlog(item, items[item], f'expected Value itemBuyEvent or itemViewEvent')
            else:
                Errorlog(item, items[item], 'Unexpected Value')
        else:
            Errorlog(item, items[item], 'Unknown Variable')
if Error == []:
    print('Pass')
else:
    print('Fail')
    print(Error)
