from app import flask
 
APP = flask.create_app()
APP.run(
    host="0.0.0.0",
    port=os.environ.get("PORT"),
    debug=True,
    use_reloader=True
)
