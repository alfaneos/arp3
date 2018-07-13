import falcon



api = application = falcon.API()

images = Resource()
api.add_route('/images', images)