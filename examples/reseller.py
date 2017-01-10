from examples_shared import init_parser, init_client, print_response


def list_product_configurations(client):
    """
    List product specific configurations for this reseller.
    """
    return client.reseller.product_configuration()


if __name__ == "__main__":

    parser = init_parser(description='Domain related examples.')

    args = parser.parse_args()

    client = init_client(args)

    print_response(list_product_configurations(client=client))
