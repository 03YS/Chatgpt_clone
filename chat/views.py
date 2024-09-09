from django.shortcuts import render
from openai import OpenAI
from django.http import JsonResponse
from .models import Chat

client = OpenAI(api_key='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')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )

        answer = completion.choices[0].message.content
        new_chat = Chat(message=message, response=answer)
        new_chat.save()
        return JsonResponse({'response': answer})
    return JsonResponse({'response': 'Invalid request'}, status=400)