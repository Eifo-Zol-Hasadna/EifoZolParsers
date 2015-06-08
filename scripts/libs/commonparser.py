import logging


def get_file_path(execution_path, relative_path_to_file):
    root_path = '/'.join(execution_path.split('/')[:-1])
    file_path = relative_path_to_file if len(root_path) == 0 else\
            '%s/%s' % (root_path, relative_path_to_file)
    return file_path


def setup_logger():
    logging.basicConfig(filename=get_file_path('', 'log.coop.parser'),
                        level=logging.DEBUG,
                        format='%(asctime)s %(levelname)5s: %(message)s'
                       )
    return logging.getLogger('COOP-parser')


