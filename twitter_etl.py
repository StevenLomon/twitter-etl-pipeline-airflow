import requests, re, time
import pandas as pd
import urllib.parse

twitter_url = "https://twitter.com/elonmusk"

def extract_user_id_from_url(twitter_url, max_retries=3, delay=1):
    encoded_screen_name = urllib.parse.quote(re.search(r'\.com\/(.*)', twitter_url).group(1))
    api_request_url = f"https://twitter.com/i/api/graphql/k5XapwcSikNsEsILW5FvgA/UserByScreenName?variables=%7B%22screen_name%22%3A%22{encoded_screen_name}%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Atrue%2C%22hidden_profile_subscriptions_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_is_identity_verified_enabled%22%3Atrue%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22responsive_web_twitter_article_notes_tab_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D"
    
    payload = {}
    headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'gt=1773225230032363666; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A171045711000761660; guest_id_marketing=v1%3A171045711000761660; personalization_id="v1_u6idRbYsFc6SIpMBQlS8iw=="; g_state={"i_l":0}; _ga=GA1.2.1514114894.1711604829; _gid=GA1.2.437719694.1711604829; kdt=uRpsjKE2e1bAAwYU24KPHMvX9BJo6viRO38xdRx9; lang=en; dnt=1; guest_id=v1%3A171160776817907946; auth_token=2bea663ec47a947162f0cf6ff08c82abf5e5886f; ct0=893c1767f31b106b1e9e44e9c36e0a13a0b68611cb2754faa5d654b2359a5030032e44dc9b5e2e7408740d46f2f45aba08075a9afbc55c41b2d5fccb586244ba9a4daca006a7eda0fb7d19fed641364f; twid=u%3D1154448997932773377; att=1-949UwbRxlY9yey34RqGpgD9QD6S928xp2Ewqxnby; _ga=GA1.2.1514114894.1711604829; _gid=GA1.2.437719694.1711604829; att=1-949UwbRxlY9yey34RqGpgD9QD6S928xp2Ewqxnby; auth_token=2bea663ec47a947162f0cf6ff08c82abf5e5886f; ct0=893c1767f31b106b1e9e44e9c36e0a13a0b68611cb2754faa5d654b2359a5030032e44dc9b5e2e7408740d46f2f45aba08075a9afbc55c41b2d5fccb586244ba9a4daca006a7eda0fb7d19fed641364f; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; dnt=1; g_state={"i_l":0}; gt=1773225230032363666; guest_id=v1%3A171160776817907946; guest_id_ads=v1%3A171045711000761660; guest_id_marketing=v1%3A171045711000761660; kdt=uRpsjKE2e1bAAwYU24KPHMvX9BJo6viRO38xdRx9; lang=en; personalization_id="v1_u6idRbYsFc6SIpMBQlS8iw=="; twid=u%3D1154448997932773377',
    'x-csrf-token': '893c1767f31b106b1e9e44e9c36e0a13a0b68611cb2754faa5d654b2359a5030032e44dc9b5e2e7408740d46f2f45aba08075a9afbc55c41b2d5fccb586244ba9a4daca006a7eda0fb7d19fed641364f'
    }

    for attempts in range(max_retries):
        try:
            response = requests.request("GET", api_request_url, headers=headers, data=payload)
            if response.status_code == 200:
                user_id = None

                data = response.json().get('data', {})
                if data:
                    user = data.get('user', {})
                    if user:
                        result = user.get('result', {})
                        if result:
                            user_id = result.get('rest_id')

                return user_id
            else:
                print(f"Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    time.sleep(delay)

    return None

musky_boi_user_id = extract_user_id_from_url(twitter_url)
print(musky_boi_user_id)

def extract_tweets_json_from_id(amount, user_id, max_retries=3, delay=1):
    api_request_url = f"https://twitter.com/i/api/graphql/GA3HM3gm-TtZJNVsvnF5Yg/UserTweets?variables=%7B%22userId%22%3A%22{user_id}%22%2C%22count%22%3A{amount}%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"

    payload = {}
    headers = {
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'cookie': 'd_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A171045711000761660; guest_id_marketing=v1%3A171045711000761660; personalization_id="v1_u6idRbYsFc6SIpMBQlS8iw=="; g_state={"i_l":0}; _ga=GA1.2.1514114894.1711604829; _gid=GA1.2.437719694.1711604829; kdt=uRpsjKE2e1bAAwYU24KPHMvX9BJo6viRO38xdRx9; dnt=1; guest_id=v1%3A171160776817907946; auth_token=2bea663ec47a947162f0cf6ff08c82abf5e5886f; ct0=893c1767f31b106b1e9e44e9c36e0a13a0b68611cb2754faa5d654b2359a5030032e44dc9b5e2e7408740d46f2f45aba08075a9afbc55c41b2d5fccb586244ba9a4daca006a7eda0fb7d19fed641364f; twid=u%3D1154448997932773377; att=1-949UwbRxlY9yey34RqGpgD9QD6S928xp2Ewqxnby; lang=en; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D',
    'x-csrf-token': '893c1767f31b106b1e9e44e9c36e0a13a0b68611cb2754faa5d654b2359a5030032e44dc9b5e2e7408740d46f2f45aba08075a9afbc55c41b2d5fccb586244ba9a4daca006a7eda0fb7d19fed641364f'
    }

    tweets = []
    counter = 0

    for attempts in range(max_retries):
        try:
            response = requests.request("GET", api_request_url, headers=headers, data=payload)
            if response.status_code == 200:
                tweet_list = None

                data = response.json().get('data', {})
                if data:
                    user = data.get('user', {})
                    if user:
                        result = user.get('result', {})
                        if result:
                            timeline_v2 = result.get('timeline_v2', {})
                            if timeline_v2:
                                timeline = timeline_v2.get('timeline', {})
                                if timeline:
                                    instructions = timeline.get('instructions', [])
                                    if instructions:
                                        tweet_list = instructions[2].get('entries', [])
                return tweet_list
            else:
                print(f"Received status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    time.sleep(delay)

    print(f"Attempting to fetch tweet #{counter+1} out of {amount}")

    return None

def extract_tweet_list_from_tweet_json(tweets_json):
    print(f"Length of tweet json: {len(tweets_json)}")
    print(type(tweets_json))
    tweets = []

    for dict in tweets_json:
        print(type(dict))
        tweet = {}
        id = None
        text = None
        content = dict.get('content', {})
        if content:
            itemContent = content.get('itemContent', {})
            if itemContent:
                tweet_results = itemContent.get('tweet_results', {})
                if tweet_results:
                    result = tweet_results.get('result', {})
                    if result:
                        note_tweet = result.get('note_tweet', {})
                        if note_tweet:
                            note_tweet_results = note_tweet.get('note_tweet_results', {})
                            if note_tweet_results:
                                result = note_tweet_results.get('result', {})
                                if result:
                                    id = result.get('id')
                                    text = result.get('text')
        tweet['id'] = id
        tweet['text'] = text
        tweets.append(tweet)
    
    return tweets


tweets_json = extract_tweets_json_from_id(26, musky_boi_user_id)
tweet_list = extract_tweet_list_from_tweet_json(tweets_json)
print(f"Length of tweet list: {len(tweet_list)}")
print(tweet_list)

df = pd.DataFrame(tweet_list)
df.to_csv("elonmuck.csv", index=False)