#!/usr/bin/env python

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Nsmf_PDUSession'}, pythonic_params=True)
    app.run(port=8083)


if __name__ == '__main__':
    main()
