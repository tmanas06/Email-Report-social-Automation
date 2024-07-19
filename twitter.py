from ntscraper import Nitter
import json

def main():
    nitter = Nitter()
    profile_info = nitter.get_profile_info("wallet_hunter") # enter the twitter profile you want to scrape
    tweets = nitter.get_tweets("wallet_hunter", mode='user', number=100)
    data = {
        "profile_info": profile_info,
        "tweets": tweets
    }
    with open("walt.json", "w") as file:
        json.dump(data, file, indent=4)
    return data

if __name__ == '__main__':
    data = main()
    print(data)