from flask import Flask 
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="Factory Management API", version="1.0", description="Factory Management System API")

# Define the Models for Swagger documentation
employee_model = api.model('Employee', {
    'id': fields.Integer(readOnly=True, description='The employee unique identifier'),
    'name': fields.String(required=True, description='The employee name'),
    'role': fields.String(required=True, description='The employee role'),
    'email': fields.String(required=True, description='The employee email')
})

product_model = api.model('Product', {
    'id': fields.Integer(readOnly=True, description='The employee unique identifier'),
    'name': fields.String(required=True, description='The product name'),
    'price': fields.Float(required=True, description='The product price'),
    'stock': fields.Integer(required=True, description='The product stock count')
})

customer_model = api.model('Order', {
    'id': fields.Integer(readOnly=True, description='The order unique identifier'),
    'customer_id': fields.Integer(required=True, description='ID of the customer placing the order'),
    'product_ids': fields.List(required=True, description='List of product IDs in the order'),
    'phone': fields.Integer(required=True, description='Quantity of products ordered')
})

employee_model = api.model('Customer', {
    'id': fields.Integer(readOnly=True, description='The customer unique identifier'),
    'name': fields.String(required=True, description='The customer name'),
    'role': fields.String(required=True, description='The employee role'),
    'email': fields.String(required=True, description='The employee email')
})

production_model = api.model('Production', {
    'id': fields.Integer(readOnly=True, description='The production unique identifier'),
    'product_id': fields.Integer(required=True, description='ID of the product being produced'),
    'quantity': fields.Integer(required=True, description='Quantity of the product produced'),

})

# Define Endpoints for each model
# Employee Endpoints
@api.route('/employees')
class EmployeeList(Resource):
    @api.marshal_list_with(employee_model)
    def get(self):
        """List all employee"""
        return [{"id": 1, "name": "Jhon Smith", "role": "Engineer", "email": "jhon@example.com"}]
    
    @api.expect(employee_model)
    @api.marshal_with(employee_model, code=201)
    def post(self):
        """Create a new employee"""
        return api.payload, 201
# Product Endpoints
@api.route('/products')
class ProductList(Resource):
    @api.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return [{"id": 1, "name": "Widget", "price": 9.99, "stock": 100}]
    
    @api.expect(product_model)
    @api.marshal_with(product_model, code=201)
    def post(self):
        """Create a new product"""
        return api.payload, 201
# Order Endpoints
@api.route('/orders')
class OrderList(Resource):
    @api.marshal_list_with(order_model)
    def get(self):
        """List all orders"""
        return [{"id": 1, "customer_id": 1, "product_ids": [1, 2], "quantity": 5}]

    @api.expect(order_model)
    @api.marshal_with(order_model, code=201)
    def post(self):
        """Create a new order"""
        return api.payload, 201

# Customer Endpoints with Error Responses
@api.route('/customers')
class CustomerList(Resource):
    @api.marshal_list_with(customer_model)
    def get(self):
        """List all customers"""
        return [{"id": 1, "name": "Jane Smith", "email": "jane@example.com", "phone": "555-1234"}]

    @api.expect(customer_model)
    @api.marshal_with(customer_model, code=201)
    def post(self):
        """Create a new customer"""
        data = api.payload
        if not data.get('email'):
            api.abort(400, "Email is required")
        if not data.get('name'):
            api.abort(400, "Name is required")
        if len(data['phone']) < 7:
            api.abort(422, "Phone number is too short")
        return data, 201

#  Production Endpoints
@api.route('/production')
class ProductionList(Resource):
    @api.marshal_list_with(production_model)
    def get(self):
        """List all productions"""
        return [{"id": 1, "product_id": 1, "quantity": 100}]
    
    @api.expect(production_model)
    @api.marshal_with(production_model, code=201)
    def post(self):
        """Create a new production"""
        return api.payload, 201

if __name__ == '__main__':
    app.run(debug=True)


# Responses of Example
# Employee Create (POST/employees)
# Request:
{
    "name": "Alice Smith",
    "role": "Manager",
    "email": "alice@example.com"
}

# Response:
{
    "id": 2,
    "name": "Alice Smith",
    "role": "Manager",
    "email": "alice@example.com"
}

# Customer Error Response(POST/customers)
# Error Request:
{
    "name": "Jane Doe",
    "phone": "555"
}

# Error Response:
{
    "error": "Unprocessable Entity",
    "message": "Phone number is too short"
}




    


    
