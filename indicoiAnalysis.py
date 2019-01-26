import indicoio

indicoio.config.api_key = 'YOUR_API_KEY'

# single example
indicoio.emotion("I did it. I got into Grad School. Not just any program, but a GREAT program. :-)")

# batch example
indicoio.emotion([
    "I did it. I got into Grad School. Not just any program, but a GREAT program. :-)",
    "Like seriously my life is bleak, I have been unemployed for almost a year."
])