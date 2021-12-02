import sys
import json
import unittest
import requests
sys.path.append("..")
from urllib.parse import urlparse
from src.jsonParser import jsonOps
from src.zendeskAPI import zendeskAPIOps
from src.argsParser import argumentsParser

class ZendeskAPITestCase(unittest.TestCase):
   # Class instantiation
    def __init__(self, testName, subdomain, user, pwd):
        super(ZendeskAPITestCase, self).__init__(testName)
        self.ZENDESK_SUBDOMAIN = subdomain
        self.ZENDESK_USER = user + '/token'
        self.ZENDESK_PWD = pwd

    # check list tickets
    def get_tickets_request(self):
        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets.json'

        resp = requests.get(url, auth=(self.ZENDESK_USER, self.ZENDESK_PWD))

        self.assertEqual(resp.status_code, 200)

    # check list all tickets with pagination
    def list_all_tickets_request_with_pagination(self):
        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets.json'

        while url:
            # Do the HTTP get request
            resp = requests.get(url, auth=(self.ZENDESK_USER, self.ZENDESK_PWD))

            self.assertEqual(resp.status_code, 200)

            data = resp.json()
            # paginate remaining pages of tickets
            url = data['next_page']

            if url is not None:
                result = urlparse(url)
                self.assertTrue(result, "❌ next_page url is not valid ❌")


    # check list of groups
    def list_groups(self):
        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/groups.json'

        resp = requests.get(url, auth=(self.ZENDESK_USER, self.ZENDESK_PWD))

        self.assertEqual(resp.status_code, 200)
        self.assertIn('groups', resp.json())

    # check creating a ticket
    def check_creating_ticket(self):
        url = f'https://{self.ZENDESK_SUBDOMAIN}.zendesk.com/api/v2/tickets.json'

        subject = 'Wildfire in California!'
        body = 'California wildfires destroy homes and threaten giant trees in Sequoia National Forest.'
        data = {'ticket': {'subject': subject, 'comment': {'body': body}}}
        payload = json.dumps(data)
        headers = {'content-type': 'application/json'}

        resp = requests.post(url, data=payload, auth=(self.ZENDESK_USER, self.ZENDESK_PWD), headers=headers)

        self.assertEqual(resp.status_code, 201)
        self.assertIn(subject, str(resp.json().values()))
        self.assertIn(body, str(resp.json().values()))


# top-level function
def main():
    try:
        args = argumentsParser.arguments()
        print('''ℹ️ Unit tests started ℹ️
        '''
        )

        config_json_val = jsonOps('../src/config.json')
        subdomain = config_json_val.__getvalue__("ZENDESK_SUBDOMAIN")

        # invoke unit tests
        suite = unittest.TestSuite()
        suite.addTest(ZendeskAPITestCase('get_tickets_request', subdomain, args.email, args.token))
        suite.addTest(ZendeskAPITestCase('list_all_tickets_request_with_pagination', subdomain, args.email, args.token))
        suite.addTest(ZendeskAPITestCase('list_groups', subdomain, args.email, args.token))
        suite.addTest(ZendeskAPITestCase('check_creating_ticket', subdomain, args.email, args.token))

        unittest.TextTestRunner(verbosity=2).run(suite)
        # unittest.main(module=test_example)

    except KeyboardInterrupt as keyerr:
        print('''
        ❌ User interrupted! ❌
        ''')
        raise(keyerr)
    except Exception as error:
        raise(error)

if __name__ == "__main__":
    sys.exit(main())
