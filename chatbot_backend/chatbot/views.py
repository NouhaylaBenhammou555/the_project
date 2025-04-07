from django.shortcuts import render

# Create your views here.
import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

openai.api_key = "your-openai-api-key-here"  # Set your OpenAI API key

class ChatbotView(APIView):
    def post(self, request):
        query = request.data.get("query", "")

        if not query:
            return Response({"error": "No query provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # or any other GPT model
                prompt=f"Answer the following financial and legal question in a professional tone: {query}",
                max_tokens=150,
                temperature=0.7,
            )

            answer = response.choices[0].text.strip()
            return Response({"answer": answer}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
