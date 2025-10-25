from django.shortcuts import render
from .forms import NumberForm
from pymongo import MongoClient

def bitwise_view(request):
    result = None
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [form.cleaned_data[x] for x in ['a','b','c','d','e']]
            negative = any(x < 0 for x in nums)
            avg = sum(nums) / 5
            count_pos = sum(1 for x in nums if x > 0)
            even_or_odd = ['even' if (x&1)==0 else 'odd' for x in nums]
            new_list = [x+10 for x in nums]
            new_list.sort()
            result = {
                'original': nums, 'avg': avg, 'negative': negative,
                'count_pos': count_pos, 'even_or_odd': even_or_odd,
                'sorted': new_list
            }
            client = MongoClient('mongodb://cctb:cctb2025@54.145.5.154:27017/cctbdb?authSource=cctbdb')
            db = client.cctbdb
            db.results.insert_one({'values': nums, 'result': result})
    else:
        form = NumberForm()
    return render(request, 'result.html', {'form': form, 'result': result})

