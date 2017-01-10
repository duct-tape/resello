from examples_shared import init_parser, init_client, print_response


def list_contacts(client):
    """
    List domain contacts.
    """
    return client.domain.contacts.all()

if __name__ == "__main__":
    parser = init_parser(description="List domain contacts.")

    args = parser.parse_args()

    client = init_client(args)

    print_response(list_contacts(client=client))
