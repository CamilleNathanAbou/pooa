from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify


class OrderController(Resource):

    def get_all(self):

