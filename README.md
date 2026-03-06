# AI-Powered Recipe Recommender API

A Flask-based REST API that generates recipe suggestions using OpenAI's GPT model. Input your available ingredients and get creative, AI-generated recipes with detailed instructions.

## 🚀 Features

- **Ingredient-based Recipe Generation**: Input available ingredients and get customized recipes
- **Dietary Restrictions Support**: Specify dietary preferences (vegetarian, low-carb, etc.)
- **Detailed Recipe Information**: Get cooking time, servings, difficulty level, and step-by-step instructions
- **RESTful API Design**: Clean, well-documented endpoints
- **Error Handling**: Comprehensive error responses and validation

## 📋 Prerequisites

- Python 3.7+
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

## 🛠️ Setup Instructions

1. **Install Dependencies**:
   bash
   pip install -r requirements.txt
   

2. **Configure Environment**:
   bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   

3. **Run the Application**:
   bash
   python app.py
   

## 📚 API Documentation

### Base URL

http://localhost:5000


### Endpoints

#### GET `/`
Welcome message with API information.

**Response Example**:

{
  "message": "Welcome to AI Recipe Recommender API",
  "version": "1.0.0",
  "endpoints": {...}
}


#### GET `/health`
Health check endpoint.

**Response Example**:

{
  "status": "healthy",
  "api_key_configured": true
}


#### POST `/recommend`
Get AI-generated recipe recommendations.

**Request Body**:

{
  "ingredients": ["chicken breast", "rice", "broccoli"],
  "dietary_restrictions": "low-carb" // optional
}


**Success Response** (200):

{
  "success": true,
  "recipe": "AI-generated recipe content",
  "ingredients_used": ["chicken breast", "rice", "broccoli"]
}


**Error Response** (400/500):

{
  "error": "Error description"
}


## 🧪 Testing

Run the test script to verify all endpoints:
bash
python test_api.py


## 📖 Example Usage with cURL

bash
# Get recipe recommendation
curl -X POST http://localhost:5000/recommend \
  -H "Content-Type: application/json" \
  -d '{
    "ingredients": ["salmon", "quinoa", "asparagus"],
    "dietary_restrictions": "gluten-free"
  }'


## 🔧 Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `FLASK_ENV`: Flask environment (development/production)
- `FLASK_DEBUG`: Enable debug mode (1/0)

## 🚧 Next Steps

- Add recipe rating and favorites functionality
- Implement recipe history and user preferences
- Add nutritional information calculation
- Create a simple web frontend
- Add recipe image generation
- Implement caching for better performance

## 🐛 Troubleshooting

- **"OpenAI API key not configured"**: Make sure you've set the `OPENAI_API_KEY` environment variable
- **Connection errors**: Ensure the Flask app is running on port 5000
- **JSON errors**: Check that your request body is valid JSON

## 📜 License

This project is for educational purposes. Make sure to comply with OpenAI's usage policies.