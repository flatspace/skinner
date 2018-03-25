# Standard libraries
import logging
import logging.config


def setup(app, app_logger_name='API', json_log_path=None):
    app.app.config['LOGGER_NAME'] = app_logger_name
    # need to access logger before configuring so that it is pre-created.
    # Otherwise, on first access, flask will overwrite the logging setup.
    app_logger = app.app.logger

    level = logging.DEBUG if app.debug else logging.INFO

    base_config = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s %(levelname)-7s [%(name)s]: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': level,
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            }
        },
        'root': {
            'level': level,
            'handlers': ['console'],
        },
        'loggers': {
            app_logger.name: {
                'handlers': ['console'],
            }
        }
    }

    logging.config.dictConfig(base_config)
    app_logger.info('Logging setup.')
