# Keywords you want to search for incoming tweets
RAW_TARGETS = [
    "python",
    "django",
    "programmer",
    "Mr. Robot",
]

# Keywords you are more interested in
DIRECT_REFERENCES = [
    "python",
]

# Filter the tweets that would appear as direct references but they aren't. For instance, you can find python (looking
# for the python keyword as a programming language) in a tweet about snakes
FALSE_DIRECT_REFERENCES = [
    "snake",
]
