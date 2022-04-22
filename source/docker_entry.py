import os;
import advanced_service;

properties = advanced_service.Properties();

properties.port = os.getenv('PORT', '80');
properties.server_addresse = os.getenv('SERVER_ADDRESSE', 'server');
properties.server_port = os.getenv('SERVER_PORT', '6666');

advanced_service.run(properties);