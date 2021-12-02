import sys
from src.jsonParser import jsonOps
from src.zendeskAPI import zendeskAPIOps
from src.argsParser import argumentsParser

# Print Menu function
def printMenu():
    print(
    '''
    \tSelect view options:
    \t * Press 1 to view all tickets
    \t * Press 2 to view a ticket
    \t * Type 'quit' to exit'''
    )
    
    
# top-level function
def main():
    try:
        args = argumentsParser.arguments()
        print('''ℹ️ Welcome to the ticket viewer\nℹ️ Type 'menu' to view options or 'quit' to exit'''
        )

        config_json_val = jsonOps('src/config.json')
        subdomain = config_json_val.__getvalue__("ZENDESK_SUBDOMAIN")
        
        # Initiate zendeskapi object
        zendeskapi = zendeskAPIOps(subdomain, args.email, args.token)

        while True:
            try:
                userInput = input("\n")
            except ValueError as ve:
                raise(ve)

            if userInput == 'menu':
                printMenu()

            elif userInput == '1':
                zendeskapi.viewALLTickets()                    
                printMenu()

            elif userInput == '2':
                zendeskapi.viewSelectedTicket()                
                printMenu()

            elif userInput == 'quit':
                print("Thanks for using the viewer")
                break
                
            else:
                print('''
                ❌ Incorrect option! Please enter a valid input! ❌
                ''')
                printMenu()
                #continue

    except KeyboardInterrupt as keyerr:
        print('''
        ❌ User interrupted! ❌
        ''')
        raise(keyerr)
    except Exception as error:
        raise(error)

if __name__ == "__main__":
    sys.exit(main())

