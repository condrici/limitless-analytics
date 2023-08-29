"""API Entry Point
This is the API entrypoint with all afferent routes
"""

import logging
import cProfile
import re        # used by cProfile.run

import flask_api.status
from flask import Flask, jsonify, render_template
from flasgger import Swagger
from flask_cors import CORS

from modules.DataScraper import PriceScraper
from modules.Schema import PriceSchema
from modules import Utilities
from modules.SearchAlgorithms import SearchAlgorithmFactory

####################
# INITIALIZATION
####################

app = Flask(__name__)
CORS(app)

Swagger(app, template=Utilities.get_json_from_file('documentation/swagger.json'))
# cProfile.run('re.compile("foo|bar")')


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e) -> str:
    # defining function
    return render_template("404.html")


if __name__ != '__main__':
    raise Exception("Could not start server due to unknown application name")

Utilities.initiate_logging()

####################
# HTTP ROUTES
####################


@app.route('/scraper/<path:url>/<algorithm>', methods=['GET'])
def index(url: str, algorithm: str):
    try:
        price_schema = PriceScraper(SearchAlgorithmFactory()).scrape(
            scrape_url=url, scrape_algorithm=algorithm
        )
    except BaseException as Ex:
        message = 'Something went wrong'
        Utilities.log(message + ' ' + str(Ex), logging.DEBUG)

        return jsonify(
            PriceSchema().dump(PriceSchema())
        ), flask_api.status.HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify(
        price_schema.dump(price_schema)
    ), flask_api.status.HTTP_200_OK


####################
# START APPLICATION
# 0.0.0.0 is an address used to refer to all IP addresses on the same machine
# this is needed in a docker context
####################

app.run(debug=True, port=8000, host="0.0.0.0")
