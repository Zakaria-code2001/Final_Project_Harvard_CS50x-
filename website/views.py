from flask import Blueprint, render_template
from urllib.parse import urlparse, urlunparse
from playlists_data import all_data

views = Blueprint('views', __name__)

data = all_data


def remove_query_params(url):
    parsed_url = urlparse(url)
    clean_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
    return clean_url


@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')


@views.route('/playlists')
def playlists():
    cleaned_videos = []
    for playlist in data['playlists']:
        for video in playlist['videos']:
            cleaned_videos.append(
                {'author': video['author'], 'title': video['title'], 'url': remove_query_params(video['url'])})
    return render_template('playlists.html', playlists=data['playlists'], videos=cleaned_videos, title='Playlists')


@views.route('/videos')
def videos():
    cleaned_videos = []
    for playlist in data['playlists']:
        for video in playlist['videos']:
            cleaned_videos.append(
                {'author': video['author'], 'title': video['title'], 'url': remove_query_params(video['url'])})
    return render_template('videos.html', videos=cleaned_videos, title='Videos', all_data=data)
