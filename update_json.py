import json

with open('./media/json_utrsite.json') as f:
    data = json.load(f)
    for key in data.keys():
        UTR5.objects.filter(utr5_id=key).update(utr5_anno=data[key]["annotations"])
        
        
        
        