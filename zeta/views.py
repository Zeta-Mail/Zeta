from time import time
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Email
from gtts import gTTS
import pickle

run_once = 0
emails = []

# Create your views here.

@login_required
def index(request):

    loadSpamModel()
    # emails = loadEmails()
    #print(predictions)

    return render(request, "zeta/index.html", {
        "emails": Email.objects.filter(spam=False, important=False)
    })

@login_required
def spam(request):

    return render(request, "zeta/spam.html", {
        "spams": Email.objects.filter(spam=True)
    })
    

@login_required
def trash(request):

    return render(request, "zeta/trash.html", {
        "trash": Email.objects.filter(spam=True)
    })

@login_required
def important(request):

        checkImportance()
        return render(request, "zeta/important.html", {
        "important": Email.objects.filter(spam=False, important=True)
    })

def loading(request):
        return render(request, "zeta/loading.html")
    
@login_required
def email(request, email_id):
        email = Email.objects.get(id=email_id)
        email.body = email.body.replace("<p>", "").replace("</p>", "").replace("[", "").replace("]", "").replace("<https:>", "").replace("</https:>", "").replace("*", "")
        email.save()

        bodyText = email.body
        obj = gTTS(text=bodyText, lang='en', slow=False)
        obj.save(r"C:\Users\User\Desktop\SDGP\Zeta\zeta\static\zeta\text.mp3")

        return render(request, "zeta/email.html", {
        "email": email
    })
    
@login_required
def privacy(request):
        return render(request, "zeta/privacy.html")
    
@login_required
def about(request):
        return render(request, "zeta/about.html")
    
@login_required
def reply(request):
        return render(request, "zeta/reply.html")
    
@login_required
def compose(request):
        return render(request, "zeta/compose.html")

@login_required
def contact(request):
        return render(request, "zeta/contact.html")
    
@login_required
def create(request):
        return render(request, "zeta/create.html")

def page_not_found_view(request, exception):

    return render(request, "zeta/404.html", status=404)

def server_error_view(request, *args, **argv):

    return render(request, "zeta/500.html", status=500)

def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "zeta/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "zeta/login.html")

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "zeta/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "zeta/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "zeta/register.html")
    
def loadSpamModel():

    global emails

    clf = pickle.load(open(r".\zeta\models\zeta\trained_model.pickle", "rb"))
    vectorizer = pickle.load(open(r'.\zeta\models\zeta\vectorizer.pickle', 'rb'))

    examples = vectorizer.transform(emails)
    predictions = clf.predict(examples)
    # return predictions

    # spams = []
    id = 0
    for x in predictions:
        if x == 1:
            email = Email.objects.get(id=id)
            email.spam = True
            email.save()
            # spams.append(emails[y])
        id+=1

    # print(spams)
    
def loadEmail():

    emails = ["Hello Diaz, how about a game of tennis tomorrow?",
    "Hello, click here if you want to satisfy your wife tonight",
    "We offer free viagra!!! Click here now!!!",
    "Dear Sara, I prepared the annual report. Please check the attachment.",
    "We will begin to sunset Universal Analytics in 2023",
    "Best holidays offers only here!!!",
    'We’d all like to get a $10,000 deposit on our bank accounts out of the blue, but winning a prize—especially if you’ve never entered a contest', 
    'Netflix is sending you a refund of $12.99. Please reply with your bank account and routing number to verify and get your refund', 
    'Your account is temporarily frozen. Please log in to to secure your account ', 
    'The article was published on 18th August itself',
    'Although we are unable to give you an exact time-frame at the moment, I would request you to stay tuned for any updates.',
    'The image you sent is a UI bug, I can check that your article is marked as regular and is not in the monetization program.',
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
    ]

    return emails
    
def checkImportance():

    important = []
 
    # Function that returns true if the word is found
    def isWordPresent(sentence, word):
        
        # To break the sentence in words
        s = sentence.lower().split(" ")
    
        for i in s:
    
            # Comparing the current word with the word to be searched
            if (i == word):
                return True
        return False
    
    words = ["important", "deadline", "critical", "mandatory", "must", "attention", "essential"]

    allEmails = Email.objects.all()
    for word in words:
        for email in allEmails:
            if (isWordPresent(email.body, word.lower())):
                email.important = True
                email.save()
                # important.append(email)

def loadGmail():

    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    import pickle
    import os.path
    import base64
    import email
    from bs4 import BeautifulSoup

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    subjects = []

    creds = None

    if os.path.exists('token.pickle'):

        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('F:\Spam Classification\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    result = service.users().messages().list(userId='me').execute()
    messages = result.get('messages')
    count = 0
    id = 0

    for msg in messages:
        count += 1
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        try:
            payload = txt['payload']
            headers = payload['headers']

            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']
                if d['name'] == 'Date':
                    time = d['value']

            parts = payload.get('parts')[0]
            data = parts['body']['data']
            data = data.replace("-","+").replace("_","/")
            decoded_data = base64.b64decode(data)
            soup = BeautifulSoup(decoded_data , "lxml")
            body = soup.body()
            
            print("Subject: ", subject)
            # print("From: ", sender)
            # print("Message: ", body)
            # print('\n')

            username = sender.split("<", 1)[0]
            x = time.split(" ")
            date = x[1] + " " + x[2]

            subjects.append(subject)
            Email.objects.create(id=id, subject=subject, sender=sender, username=username, body=body, time=time, date=date)
            id+= 1

        except Exception as e:
            print(e)

    return subjects

emails = loadGmail()  