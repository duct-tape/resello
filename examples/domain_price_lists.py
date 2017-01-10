from examples_shared import init_client, init_parser, print_response


def list_price_lists(client):
    """
    List domain price lists.
    """
    return client.domain.price_lists.all()


if __name__ == "__main__":
    parser = init_parser(description='Domain pricing example.')
    args = parser.parse_args()

    client = init_client(args)

    print_response(list_price_lists(client=client))
