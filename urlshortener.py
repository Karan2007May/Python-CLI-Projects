# URL Shortener
url_mapping = {}  
def shorten_url(original_url):
   short_url = ''.join(random.choice(string.ascii_letters) for _ in range(6))
   url_mapping[short_url] = original_url
   return short_url  # Example usage
original_url = input("Enter the original URL: ") #Ask for the full URL
shortened_url = shorten_url(original_url)
print(f"Shortened URL: {shortened_url}")

