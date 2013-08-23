
import logging, logging.handlers
from socket import error as socket_error
from datetime import datetime

def add_argparse_group(parser):
    """Add a configuration group for plumb_util to an argparser"""
    group = parser.add_argument_group('find_service', 'SRV lookup configuration')
    group.add_argument('-D', '--domain', type = str, dest = 'zone', default = None,
                       help = 'DNS domain to consult for service autodiscovery.')
    group.add_argument('-L', '--loglevel', dest='log_level', default='error',
                       choices=['debug', 'info', 'warn', 'error'],
                       help = 'Set the syslog logging level.')


# Add sub-second time logging.
#
# Unfortunately time tuples don't contain sub-second resolution, and
# logging.Formatter insists on using time tuples. So we override.
class LogFormatter(logging.Formatter):
    def formatTime(self, record, dateFmt):
        timestamp = datetime.fromtimestamp(record.created)
        return timestamp.strftime(dateFmt)


def init_logging(level, procname):
    logger = logging.root
    str_fmt = '%(asctime)s. ' + procname + ': ' + logging.BASIC_FORMAT
    date_fmt = '%b %d %H:%M:%S.%3f'
    log_fmt = LogFormatter(str_fmt, date_fmt)
    try:
        h1 = logging.handlers.SysLogHandler(address='/dev/log',
                facility=logging.handlers.SysLogHandler.LOG_LOCAL0)
    except socket_error:
        h1 = None

    h2 = logging.StreamHandler()
    h2.setFormatter(log_fmt)
    logger.addHandler(h2)
    if h1 is not None:
        h1.setFormatter(log_fmt)
        logger.addHandler(h1)
    logger.setLevel(level)
    if h1 is None:
        logger.warn('unable to initialize syslog logger')
    return logger

def logger_from_args(args, procname):
    # Set the log level
    if args.log_level == 'debug':
        level=logging.DEBUG
    elif args.log_level == 'info':
        level=logging.INFO
    elif args.log_level == 'warn':
        level=logging.WARN
    elif args.log_level == 'error':
        level=logging.ERROR
    return init_logging(level, procname)

