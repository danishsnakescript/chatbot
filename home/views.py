from django.shortcuts import render , HttpResponse
from django.http import JsonResponse , StreamingHttpResponse
import openai
# Create your views here.

openai.api_key = ""
 
def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        stream=True  # Request streaming response from OpenAI
    )

    def generate_chunks():
        for chunk in response:
            yield chunk.choices[0].delta.get("content", "")

    return StreamingHttpResponse(generate_chunks(), content_type="text/plain")


def index(request):
    if request.method == "POST":
        message = request.POST.get("message")
        return ask_openai(message)
    return render(request, "chatbot.html")






# def ask_openai(message):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": message},
#         ],
#     )
#     answer = response.choices[0].message["content"].strip()
#     return answer


# def index(request):
#     if request.method =="POST":
#         message = request.POST.get("message")
#         response = ask_openai(message)
#         return JsonResponse({'message':message,'response':response})
#     return render(request,"chatbot.html")