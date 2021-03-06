import logging 
import logstash
import sys
import time

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.TCPLogstashHandler('34.233.141.90', 5010, version=1))

test_logger.error('python-logstash: test logstash error message')
#test_logger.info('python-logstash: test logstash info message')
#test_logger.warning('python-logstash: test logstash warning message')

#test_logger.info('python')

extra = {
	'test_string': 'python version ' + repr(sys.version_info),
	'test_boolean': True,
	'test_dict': {'a': 1, 'b': 'c'},
	'test_float': 1.23,
	'test_integer': 126,
	'test_list': [1, 2, 3]

}

test_logger.info('python-logstash: test extra fileds', extra=extra)
