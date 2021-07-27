from django.shortcuts import render, redirect
from django.contrib import messages

import datetime

from .forms import NewTweetForm, SearchForm, UpdateForm
from .models import Tweet
from django.contrib.auth.models import User


def home(response):
    if not response.user.is_authenticated: return redirect('/login')
    new_tweet_form = NewTweetForm()
    search_form = SearchForm()

    if response.method == 'POST' and 'tweet_text' in response.POST.keys():
        new_tweet_form = NewTweetForm(response.POST)
        if new_tweet_form.is_valid():
            new_tweet = Tweet(tweet_text=new_tweet_form.cleaned_data['tweet_text'],author=response.user)
            new_tweet.save()
        else:
            messages.add_message(response, messages.ERROR, '[ERROR] Unable to add tweet.')
        return redirect('/home')

    elif response.method == 'POST' and 'search_text' in response.POST.keys():
        search_form = SearchForm(response.POST)
        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']
            return redirect(f'/search/{search_text}')
        else:
            messages.add_message(response, messages.ERROR, '[ERROR] Unable to complete search.')

    else:
        home_tweets = Tweet.objects.filter(author=response.user).order_by('date_created')
        return render(response, 'home.html', {'new_tweet_form': new_tweet_form,
                                              'search_form': search_form,
                                              'home_tweets': home_tweets})


def explore(response):
    if not User.is_authenticated: return redirect('/login')
    search_form = SearchForm()

    if response.method == 'POST' and 'search_text' in response.POST.keys():
        search_form = SearchForm(response.POST)
        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']
            return redirect(f'/search/{search_text}')
        else:
            messages.add_message(response, messages.ERROR, '[ERROR] Unable to complete search.')

    else:
        explore_tweets = Tweet.objects.order_by('date_created')
        return render(response, 'explore.html', {'search_form': search_form,
                                                 'explore_tweets': explore_tweets})


def search(response, search_text):
    if not User.is_authenticated: return redirect('/login')
    search_form = SearchForm()

    if response.method == 'POST' and 'search_text' in response.POST.keys():
        search_form = SearchForm(response.POST)
        if search_form.is_valid():
            search_text = search_form.cleaned_data['search_text']
            return redirect(f'/search/{search_text}')
        else:
            messages.add_message(response, messages.ERROR, '[ERROR] Unable to complete search.')
    else:
        search_tweets = Tweet.objects.filter(tweet_text__icontains=search_text).order_by('date_created')
        return render(response, 'search.html', {'search_text': search_text,
                                                'search_form': search_form,
                                                'search_tweets': search_tweets})


def delete(response, id):
    try:
        tweet_to_delete = Tweet.objects.get(id=id)
        tweet_to_delete.delete()
    except:
        messages.add_message(response, messages.ERROR, '[ERROR] Unable to delete tweet.')
    return redirect('/home')


def update(response, id):
    tweet_to_update = Tweet.objects.get(id=id)
    update_form = UpdateForm({'update_text': tweet_to_update.tweet_text})

    if response.method == 'POST' and 'submit' in response.POST:
        update_form = UpdateForm(response.POST)
        if update_form.is_valid():
            updated_tweet_text = update_form.cleaned_data['update_text']
            if tweet_to_update.tweet_text != updated_tweet_text:
                tweet_to_update.tweet_text = updated_tweet_text
                tweet_to_update.date_created = datetime.datetime.utcnow()
                tweet_to_update.save()
            else:
                messages.add_message(response, messages.ERROR, '[ERROR] Unable to update.')
        return redirect('/home')

    elif response.method == 'POST' and 'cancel' in response.POST:
        return redirect('/home')

    else:
        return render(response, 'update.html', {'update_form': update_form})
