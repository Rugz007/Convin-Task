from django.shortcuts import redirect, render
from requests.api import head
from .models import Account, Contact, User
from rest_framework import viewsets, status as http_status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, JSONParser
import requests
import json
from django.shortcuts import redirect
import os

# Create your views here.
class MatchesViewSet(viewsets.ViewSet):
    parser_classes = (FormParser, JSONParser)

    def authorize(self, request):
        """
        Request to create a match if a user swipes
        """
        client_id = os.environ["CLIENT_ID"]
        redirect_url = "http://localhost:8000/salesforce/callback"
        return redirect(
            f"https://login.salesforce.com/services/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code"
        )

    def authenticate(self, request):
        code = request.GET["code"]
        client_id = os.environ["CLIENT_ID"]
        redirect_url = "http://localhost:8000/salesforce/callback"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        client_secret = os.environ["CLIENT_SECRET"]
        body = {
            "grant_type": "authorization_code",
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_url,
        }
        response = requests.post("https://login.salesforce.com/services/oauth2/token", headers=header, data=body)
        response = json.loads(response.text)
        authentication = {"Authorization": "Bearer " + response["access_token"]}
        response_users = requests.get(
            "https://tset7-dev-ed.my.salesforce.com/services/data/v53.0/query?q=SELECT+UserName+FROM+User",
            headers=authentication,
        )
        response_users = json.loads(response_users.text)
        response_accounts = requests.get(
            "https://tset7-dev-ed.my.salesforce.com/services/data/v53.0/query?q=SELECT+name+FROM+Account",
            headers=authentication,
        )
        response_accounts = json.loads(response_accounts.text)
        response_contacts = requests.get(
            "https://tset7-dev-ed.my.salesforce.com/services/data/v53.0/query?q=SELECT+name+FROM+Contact",
            headers=authentication,
        )
        response_contacts = json.loads(response_contacts.text)
        users = []
        accounts = []
        contacts = []
        for user in response_users["records"]:
            users.append(User(username=user["Username"]))
        User.objects.bulk_create(users)
        for account in response_accounts["records"]:
            accounts.append(Account(name=account["Name"]))
        Account.objects.bulk_create(accounts)
        for contact in response_contacts["records"]:
            contacts.append(Contact(name=contact["Name"]))
        Contact.objects.bulk_create(contacts)
        return Response(
            {"Users": response_users, "Accounts": response_accounts, "Contacts": response_contacts},
            status=http_status.HTTP_200_OK,
        )

