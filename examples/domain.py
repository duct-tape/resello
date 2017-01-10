import logging
from examples_shared import init_client, init_parser, print_response


def domains(client):
    """
    Get list of domains owned by current reseller.
    """
    return client.domain.all()


def register_domain(client, name, interval, contact_id):
    """
    Register domain with given name, interval
     and use same contact id for all contacts.
    """
    return client.domain.create_domain(
        name=name,
        interval=interval,
        is_managed=False,
        contacts=[
            {u'contact': contact_id, u'role': u'registrant'},
            {u'contact': contact_id, u'role': u'admin'},
            {u'contact': contact_id, u'role': u'tech'},
            {u'contact': contact_id, u'role': u'billing'}
        ]
    )


def details(client, domain_id):
    """
    Get domain details by reference.
    """
    return client.domain.details(uuid=domain_id)


if __name__ == "__main__":

    parser = init_parser(description='Domain related examples.')
    parser.add_argument(
        'commands',
        type=str,
        nargs='+',
        choices=['domains', 'register_domain', 'details'],
        help='Command to execute.'
    )

    args = parser.parse_args()

    client = init_client(args)

    if 'domains' in args.commands:
        response = domains(client=client)
        print_response(response)

    if 'register_domain' in args.commands:
        print("Domain name?")
        domain_name = raw_input('> ')
        print("Interval? Leave empty for 12.")
        interval = raw_input('> ')
        print("Contact id?")
        contact_id = raw_input('> ')
        logging.info(
            "Creating domain {} with interval {} and contact id: {}".format(
                domain_name,
                interval,
                contact_id
            )
        )
        response = register_domain(client=client,
                                   name=domain_name,
                                   interval=interval,
                                   contact_id=contact_id)
        print_response(response)

    if 'details' in args.commands:
        print("Domain id?")
        domain_id = raw_input('> ')
        logging.info("Requesting domain details for {}".format(domain_id))
        response = details(client=client, domain_id=domain_id)
        print_response(response)
