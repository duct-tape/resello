from examples_shared import init_parser, init_client, print_response


def list_instances(client):
    """
    List all VPS instances.
    """
    return client.vps.instances()


def details(client, instance_id):
    """
    Get instance details.
    """
    return client.vps.details(instance_id=instance_id)


def get_access(client, instance_id):
    """
    Get intance VNC console URI.
    """
    return client.vps.get_access_url(instance_id=instance_id)


if __name__ == "__main__":

    parser = init_parser(description='Domain related examples.')
    parser.add_argument(
        'commands',
        type=str,
        nargs='+',
        choices=['list_instances', 'get_access', 'details'],
        help='Command to execute.'
    )

    args = parser.parse_args()

    client = init_client(args)

    if 'list_instances' in args.commands:
        print_response(list_instances(client=client))

    if 'get_access' in args.commands:
        print("Instance id?")
        instance_id = raw_input('> ')
        print_response(get_access(client=client, instance_id=instance_id))

    if 'details' in args.commands:
        print("Instance id?")
        instance_id = raw_input('> ')
        print_response(details(client=client, instance_id=instance_id))
