from examples_shared import init_parser, init_client, print_response


def details(client, tld_name):
    """
    Get TLD details.
    """
    return client.domain.tld(tld_name=tld_name)

if __name__ == "__main__":

    parser = init_parser(description='Domain related examples.')
    parser.add_argument('tlds', nargs='+', type=str, help='List of tlds.')

    args = parser.parse_args()

    client = init_client(args)

    for tld_name in args.tlds:
        print_response(details(client=client, tld_name=tld_name))
