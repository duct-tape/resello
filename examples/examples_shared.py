import argparse
import logging
import os
from pprint import pprint
from resello import ReselloClient
import sys


def init_parser(description):
    """
    Initialize arg parser.
    """
    parser = argparse.ArgumentParser(
        description=description
    )
    parser.add_argument('--debug', dest='debug', action='store_true',
                        default=False,
                        help='Enable debug.')
    parser.add_argument('--host', dest='host', action='store',
                        default='https://rp01.hostcontrol.com',
                        help='API Hostname.')
    parser.add_argument('--ref', dest='reseller_reference', action='store',
                        default=os.environ.get('REFERENCE', None),
                        help='Reseller reference. Env: REFERENCE')

    parser.add_argument('--key', dest='api_key', action='store',
                        default=os.environ.get('API_KEY', None),
                        help='API key. Env: API_KEY')
    return parser


def init_client(args):
    """
    Initiates client using bypassed parameters.
    """
    if args.debug:
        print("Setting log level to debug.")
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug mode enabled.")

    logging.debug("Initiating client. Args: {}".format(args))
    if args.api_key is None or args.reseller_reference is None:
        print("Failed to initiate client. \n"
              "Please provide Reference and API Key.\n")
        sys.exit(1)

    logging.info(
        "Initiating resello client with reference: {} and api key {}".format(
            args.reseller_reference,
            args.api_key,
        )
    )
    client = ReselloClient(
        api_key=args.api_key,
        reseller_reference=args.reseller_reference,
    )
    if args.host is not None:
        client.BASE_PATH = "{}/api/v1".format(args.host)
    return client


def print_response(response):
    logging.debug("Raw response: {}".format(response._response.text))
    if response.has_errors:
        print("Errors in response: {}".format(response.errors))

    pprint(response)
