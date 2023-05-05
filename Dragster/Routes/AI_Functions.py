from .Tool.Tools import get_stackoverflow_link, get_example_code_gfg, get_answer_from_given_link
from django.shortcuts import render
from django.http import JsonResponse
import wikipedia
from googlesearch import search
import requests
from bs4 import BeautifulSoup


def get_content(query):
    # Search Google for web pages related to the query
    urls = list(search(query, num_results=3))
    print("Web Scrap started")
    # Scrape the contents of each web page
    content = []
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Extract the text content from the page
            text = soup.get_text()
            content.append(text)
        except:
            # Skip any pages that cannot be accessed
            pass
    try:
        # return content
        return "".join(content[0].split(".")[0:3])
    except:
        try:
            return content
        except:
            return "I can't understand please try any differnt question or give me more detials about your question"

def Code_scriping(request):
    context = {}
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            # Get the Stack Overflow link for the question
            link = get_stackoverflow_link(question)
            link_gfg = get_stackoverflow_link(question, 'geeksforgeeks.org')
            if link:
                # Get the example code from the link
                code = get_answer_from_given_link(link)
                code_gfg = get_example_code_gfg(link_gfg)
                if code:
                    # Add the question, link and code to the context
                    context['question_s'] = question
                    context['link_s'] = link
                    context['code_s'] = code
                else:
                    context['error'] = "request timeout {-_-}... can't scarp the queary at a moment"
                if code_gfg:
                    # Add the question, link and code to the context
                    context['question_gfg'] = question
                    context['link_gfg'] = link
                    context['code_gfg'] = code_gfg
            else:
                context['error'] = "request timeout {-_-}... can't scarp the queary at a moment"
        else:
            context['error'] = 'Please enter a question'
    return render(request,  'AI_Functions/CodeScriping.html', context)

def chatbot_res(request):
    if request.method == "GET":
        message = request.GET.get("message")
        print(message)
        link = get_stackoverflow_link(message)
        code = get_answer_from_given_link(link)
        # process the user input and generate a response
        print("\n\n\n\n\n\n\n\n\n\n\n",code)
        if code:
            response = code
        else:
            try:
                wikipedia.set_lang("en")
                # Get the summary of a page
                page = wikipedia.page(message)
                summary = page.summary
                response = summary
                return JsonResponse({"response": response})
            except:
                return JsonResponse({"response":get_content(message)})
    else:
        return JsonResponse({"error": "Invalid request method"})

def Error_Solver(request):
    context = {}
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            # Get the Stack Overflow link for the question
            link = get_stackoverflow_link(question)
            link_gfg = get_stackoverflow_link(question, 'geeksforgeeks.org')
            if link:
                # Get the example code from the link
                code = get_answer_from_given_link(link)
                code_gfg = get_example_code_gfg(link_gfg)
                if code:
                    # Add the question, link and code to the context
                    context['question_s'] = question
                    context['link_s'] = link
                    context['code_s'] = code
                else:
                    context['error'] = "request timeout {-_-}... can't scarp the queary at a moment"
                if code_gfg:
                    # Add the question, link and code to the context
                    context['question_gfg'] = question
                    context['link_gfg'] = link
                    context['code_gfg'] = code_gfg
            else:
                context['error'] = "request timeout {-_-}... can't scarp the queary at a moment"
        else:
            context['error'] = 'Please enter a question'
    return render(request,  'AI_Functions/Error_Solver.html', context)
