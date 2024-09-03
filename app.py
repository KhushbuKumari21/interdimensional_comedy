from flask import Flask, jsonify, render_template
from flask_smorest import Api, Blueprint
from flask_cors import CORS
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['API_TITLE'] = 'Interdimensional Comedy API'
app.config['API_VERSION'] = '1.0.0'
app.config['OPENAPI_VERSION'] = '3.0.3'
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


blp = Blueprint('comedy', 'comedy', url_prefix='/api', description='Operations on Comedy Shows')

# Define the schema for the input data using Marshmallow
class ComedyRequestSchema(Schema):
    style = fields.Str(required=True, metadata={"description": "Type of comedy"})
    gender = fields.Str(required=True, metadata={"description": "Gender of the performer"})
    dimension = fields.Int(required=True, metadata={"description": "Dimension in which the show takes place"})

# API route for generating comedy show
@blp.route('/generate_comedy', methods=['POST'])
@blp.arguments(ComedyRequestSchema, location='json')
@blp.response(200, description='Comedy Show Generated Successfully')
def generate_comedy(data):
    style = data.get('style')
    gender = data.get('gender')
    dimension = data.get('dimension')

    # Generate the comedy show message
    comedy_show = (
        f"Welcome to the {dimension}th dimension! Tonight's show features a {gender} comedian delivering "
        f"{style} comedy that'll make your interdimensional travels unforgettable!"
    )
    return jsonify({'comedy_show': comedy_show})

# Register the blueprint with the API
api.register_blueprint(blp)

if __name__ == '__main__':
    app.run(debug=True)
