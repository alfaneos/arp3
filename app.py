import falcon

from images import Resource


api = wsgi_app = falcon.API()
images = Resource()
api.add_route('/images', images)