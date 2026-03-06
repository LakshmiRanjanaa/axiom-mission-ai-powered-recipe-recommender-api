from flask import Flask, request, jsonify
import openai
import os
from typing import List, Dict

# Initialize Flask app
app = Flask(__name__)

# Set up OpenAI API key (you'll need to add your key to environment variables)
openai.api_key = os.getenv('OPENAI_API_KEY')

class RecipeRecommender:
    """Handles AI-powered recipe recommendations using OpenAI API"""
    
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    def generate_recipe_prompt(self, ingredients: List[str], dietary_restrictions: str = "") -> str:
        """Creates a structured prompt for OpenAI to generate recipes"""
        ingredients_str = ", ".join(ingredients)
        prompt = f"""
        Create a detailed recipe using these ingredients: {ingredients_str}
        
        Additional requirements:
        - Dietary restrictions: {dietary_restrictions if dietary_restrictions else "None"}
        - Include cooking time, servings, and difficulty level
        - Provide step-by-step instructions
        - Suggest additional ingredients if needed
        
        Format the response as a JSON object with: title, ingredients, instructions, cooking_time, servings, difficulty.
        """
        return prompt.strip()
    
    def get_recipe_suggestions(self, ingredients: List[str], dietary_restrictions: str = "") -> Dict:
        """Calls OpenAI API to get recipe suggestions"""
        try:
            prompt = self.generate_recipe_prompt(ingredients, dietary_restrictions)
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional chef assistant. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return {
                "success": True,
                "recipe": response.choices[0].message.content,
                "ingredients_used": ingredients
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to generate recipe: {str(e)}"
            }

# Initialize the recommender
recommender = RecipeRecommender()

@app.route('/', methods=['GET'])
def home():
    """Welcome endpoint with API information"""
    return jsonify({
        "message": "Welcome to AI Recipe Recommender API",
        "version": "1.0.0",
        "endpoints": {
            "/": "GET - This welcome message",
            "/health": "GET - Health check",
            "/recommend": "POST - Get recipe recommendations"
        }
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        "status": "healthy",
        "api_key_configured": bool(os.getenv('OPENAI_API_KEY'))
    })

@app.route('/recommend', methods=['POST'])
def recommend_recipe():
    """Main endpoint for recipe recommendations"""
    try:
        # Parse JSON request
        data = request.get_json()
        
        # Validate required fields
        if not data or 'ingredients' not in data:
            return jsonify({
                "error": "Missing required field: ingredients",
                "example": {
                    "ingredients": ["chicken", "rice", "vegetables"],
                    "dietary_restrictions": "vegetarian (optional)"
                }
            }), 400
        
        ingredients = data.get('ingredients', [])
        dietary_restrictions = data.get('dietary_restrictions', "")
        
        # Validate ingredients list
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            return jsonify({
                "error": "Ingredients must be a non-empty list"
            }), 400
        
        # Check if OpenAI API key is configured
        if not os.getenv('OPENAI_API_KEY'):
            return jsonify({
                "error": "OpenAI API key not configured. Please set OPENAI_API_KEY environment variable."
            }), 500
        
        # Get recipe recommendations
        result = recommender.get_recipe_suggestions(ingredients, dietary_restrictions)
        
        if result['success']:
            return jsonify(result), 200
        else:
            return jsonify(result), 500
            
    except Exception as e:
        return jsonify({
            "error": f"Internal server error: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)