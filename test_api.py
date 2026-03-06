import requests
import json

# Test script for the Recipe Recommender API
# Run this after starting your Flask app to test the endpoints

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_home_endpoint():
    """Test the home endpoint"""
    print("\n=== Testing Home Endpoint ===")
    response = requests.get(BASE_URL)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_recipe_recommendation():
    """Test the recipe recommendation endpoint"""
    print("\n=== Testing Recipe Recommendation ===")
    
    # Test data
    test_payload = {
        "ingredients": ["chicken breast", "rice", "broccoli", "garlic"],
        "dietary_restrictions": "low-carb"
    }
    
    response = requests.post(
        f"{BASE_URL}/recommend",
        json=test_payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_invalid_request():
    """Test error handling with invalid request"""
    print("\n=== Testing Invalid Request ===")
    
    # Missing ingredients field
    invalid_payload = {
        "dietary_restrictions": "vegetarian"
    }
    
    response = requests.post(
        f"{BASE_URL}/recommend",
        json=invalid_payload,
        headers={"Content-Type": "application/json"}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    print("Starting API Tests...")
    print("Make sure your Flask app is running on localhost:5000")
    
    try:
        test_home_endpoint()
        test_health_check()
        test_invalid_request()
        test_recipe_recommendation()  # This will fail without OpenAI API key
        
    except requests.exceptions.ConnectionError:
        print("\nError: Could not connect to the API.")
        print("Make sure your Flask app is running with: python app.py")
    except Exception as e:
        print(f"\nUnexpected error: {e}")