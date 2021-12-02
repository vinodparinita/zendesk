import argparse

class argumentsParser():

    # Arguments Handler function
    def arguments():
        parser = argparse.ArgumentParser(
            description="Zendesk Ticket Viewer"
        )
        parser.add_argument(
            "-u",
            "--email",
            default="all",
            type=str,
            help="Email ID of Zendesk user account"
        )
        parser.add_argument(
            "-t",
            "--token",
            default="all",
            type=str,
            help="API Token of Zendesk user account"
        )
        return(parser.parse_args())
