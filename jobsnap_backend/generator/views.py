import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

# 🧠 Create OpenAI client using environment variable
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@csrf_exempt
def generate_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt")
            tone = data.get("tone")
            mode = data.get("mode")

            if not prompt or not tone or not mode:
                return JsonResponse({"status": "error", "message": "Prompt, tone and mode are required."})

            full_prompt = f"Generate a {tone} style {mode} based on the following job description:\n{prompt}"

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert resume writer."},
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )

            ai_response = response.choices[0].message.content
            return JsonResponse({"status": "success", "description": ai_response})

        except Exception as e:
            return JsonResponse({"status": "error", "message": f"AI generation failed: {str(e)}"})

    return JsonResponse({"status": "error", "message": "Only POST method allowed."})
