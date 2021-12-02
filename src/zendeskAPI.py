import sys
import requests
from datetime import datetime

class zendeskAPIOps:
    # Class instantiation
    def __init__(self, subdomain, user, pwd):
        self.ZENDESK_SUBDOMAIN = subdomain
        self.ZENDESK_USER = user + '/token'
        self.ZENDESK_PWD = pwd

    # ZENDESK API GET requests
    def apiGETRequest(self, url):
        try:
            #headers = {'content-type': 'application/json'}
            #response = requests.get(url, auth=(user, pwd), headers=headers)
            response = requests.get(url, auth=(self.ZENDESK_USER, self.ZENDESK_PWD))

            # Check for HTTP codes other than 200 (Success)
            if response.status_code != 200:
                print('❌ Status:' , \
                      response.status_code, \
                      'Problem with the request. Exiting ❌'
                      )
                exit()
            try:
                return response
            except Exception as e:
                return e.args[0]
        except requests.exceptions.RequestException as e:
            raise("❌ Error occurred: {} ❌".format(e))


    # view ALL ZENDESK Tickets
    def viewALLTickets(self):
        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets.json'

        while url:
            # Do the HTTP get request
            response = self.apiGETRequest(url)
            data = response.json()
            
            # iterate through each ticket from tickets list
            for each_ticket in data['tickets']:
                print('Ticket with subject', \
                      "'{}'".format(each_ticket['subject']), \
                      'opened by', \
                      each_ticket['requester_id'], \
                      'on', \
                      datetime.strptime(each_ticket['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y %I:%M%p')
                      )

            # paginate remaining pages of tickets
            url = data['next_page']


    # view a selected ZENDESK Ticket
    def viewSelectedTicket(self):
        ticketNumber = input("Enter ticket number:\n")

        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets/{ticketNumber}.json'

        # Do the HTTP get request
        response = self.apiGETRequest(url)
        data = response.json()
        
        print('Ticket with subject', \
              "'{}'".format(data['ticket']['subject']), \
              'opened by', \
              data['ticket']['requester_id'], \
              'on', \
              datetime.strptime(data['ticket']['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y %I:%M%p')
              )

        #message = f'Ticket with subject '{data['ticket']['subject']}' opened by {data['ticket']['requester_id']} on {datetime.strptime(data['ticket']['created_at'], '%Y-%m-%dT%H:%M:%SZ').strftime('%d %b %Y %I:%M%p')}'
        #print(message)


if __name__ == "__main__":
    sys.exit(main())
