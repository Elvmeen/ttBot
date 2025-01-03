#!/usr/bin/env python
# coding: utf-8

from func import generate_prompt, generate_tweet_from_openai, post_tweet  # Import the necessary functions from func.py

if __name__ == "__main__":
    # Generate a random tweet prompt
    tweet_prompt = generate_prompt()

    # Generate the tweet content using OpenAI's GPT (passing the prompt to OpenAI for content generation)
    tweet = generate_tweet_from_openai(tweet_prompt)

    # Post the generated tweet using the Twitter API
    post_tweet(tweet)  # Now it will work with the tweet generated by OpenAI
