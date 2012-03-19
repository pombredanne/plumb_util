
def add_argparse_group(parser):
    """Add a configuration group for plumb_util to an argparser"""
    group = parser.add_argument_group('find_service', 'SRV lookup configuration')
    group.add_argument('-D', '--domain', type = str, dest = 'zone', default = None,
                       help = 'DNS domain to consult for service autodiscovery.')
