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

musky_boi_user_id = extract_user_id_from_url(twitter_url)
print(musky_boi_user_id)
