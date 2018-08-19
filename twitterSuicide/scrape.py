import twitter

# Load keys as a OS variable
api = twitter.Api(consumer_key=[consumer key],
                  consumer_secret=[consumer secret],
                  access_token_key=[access token],
                  access_token_secret=[access token secret])

# Filter by:  "location": "Denver, CO"
# Try: bio_location:chicago profile_region:illinois profile_locality:chicago

