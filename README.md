# EC601Phase1a
These are some test done with TwitterAPI.

I tried to get the user information by its *SCREEN_NAME*, and the API brings me my profile like:

[{'id': 1310426119800197120, 'id_str': '1310426119800197120', 'name': 'tianhel', 'screen_name': 'tianhel1', 'location': '', 'description': 'nb', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 0, 'friends_count': 6, 'listed_count': 0, 'created_at': 'Mon Sep 28 03:48:33 +0000 2020', 'favourites_count': 0, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 0, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1310426311274295297/adYZ6A-7_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1310426311274295297/adYZ6A-7_normal.jpg', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None, 'translator_type': 'none'}]

I also tried to retrive one single tweet by its *TWEET_ID*. The ID is shown in the url when you read a certain tweet.

And I used the search function to get last 10 tweets about Trump using *SEARCH_TERM*, it works.

# EC601Phase1b

I tried the NLP API in "Hello, world!".

PS G:\2020FAll\EC601> python NLPTest.py

Text: Hello, world!

Sentiment: 0.6000000238418579, 0.6000000238418579

