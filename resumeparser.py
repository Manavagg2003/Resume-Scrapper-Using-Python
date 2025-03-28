import requests
import yaml
import json

CONFIG_PATH = "config.yaml"

# Extraction template for consistent JSON output
EXTRACTION_TEMPLATE = """Extract the following ATS fields as JSON:
{
  "name": "Full name",
  "email": "Email address",
  "skills": ["list", "of", "skills"],
  "experience": ["Position details"],
  "education": ["Degree details"]
}"""

def load_api_key():
    try:
        with open(CONFIG_PATH) as file:
            data = yaml.safe_load(file)
            api_key = data.get('OPENROUTER_API_KEY') or data.get('openrouter')  # Common key names
            
            if not api_key:
                raise ValueError("Add your OpenRouter API key to config.yaml:\nopenrouter: sk-or-...")
                
            return api_key
            
    except Exception as e:
        raise RuntimeError(f"Config error: {str(e)}")

def ats_extractor(resume_data):
    try:
        api_key = load_api_key()
        
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "HTTP-Referer": "YOUR_SITE_URL",  # Required by OpenRouter
                "X-Title": "ATS Parser"  # Identify your app
            },
            json={
                "model": "openai/gpt-4",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an ATS parser. Return ONLY valid JSON. Do not include explanations."
                    },
                    {
                        "role": "user",
                        "content": f"{EXTRACTION_TEMPLATE}\n\nResume data:\n{resume_data}"
                    }
                ],
                "temperature": 0.1,
                "max_tokens": 2000
            },
            timeout=20
        )

        # Check for API errors
        if 400 <= response.status_code < 500:
            error_data = response.json().get('error', {})
            return {
                "error": f"API Client Error: {error_data.get('message', 'Unknown error')}",
                "code": error_data.get('code'),
                "type": error_data.get('type')
            }

        response.raise_for_status()
        
        content = response.json()["choices"][0]["message"]["content"]
        
        # Clean JSON response (sometimes contains markdown backticks)
        cleaned = content.strip().replace('```json', '').replace('```', '')
        
        return {
            "data": json.loads(cleaned),
            "raw_response": content  # For debugging
        }

    except json.JSONDecodeError:
        return {"error": "API returned invalid JSON", "raw_content": content}
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
        
    except Exception as e:
        return {"error": f"Processing failed: {str(e)}"}