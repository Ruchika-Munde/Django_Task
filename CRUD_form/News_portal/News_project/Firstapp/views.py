from django.shortcuts import render

# Create your views here.
def display_view(request):
    return render(request,'display.html')

def top_news(request):
    news1='GST revenue collection crossed Rs 1 lakh crore in November.'
    news2='Cong leader Nana Patole elected as Maharashtra assembly speaker.'
    news3='Jay shah to represent BCCI at ICC CEC meeting.'
    news4='23 top-end and mid-range phones from Apple,Realme, Samsung and others that got price cuts in 2019.'

    return render(request,'Top news.html',{'news1':news1,'news2':news2,'news3':news3,'news4':news4})

def politics_news(request):
    news1='Game changer:Ajit packs pawar play with late, reverse swinger.'
    news2='Fadanvis haste to come to power sank BJP in Maharashtra:sanjay Raut'
    news3='NCP yet to decide name for deputy CM post, says Jayant Patil'
    news4='Thackeray-pawar ties: Acreoss generations,families have melded political with personal'
    return render(request, 'Politics.html', {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4})

def trending_news(request):
    news1= 'CAT III-trained captain flying as passenger asked to operate IndiGo Flight as visibility drops at IGI Airport'
    news2= 'Amazon is making shopping easier for Android users'
    news3= 'Global cybersecurity firm palo alto networks suffers data breach'
    news4= 'Hurry! Big Discounts on 2/3 BHK Homes in pune at 50L onwards'
    return render(request, 'trending.html', {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4})